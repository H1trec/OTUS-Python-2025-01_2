from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.messages import constants as message_constants
from django.urls import path, reverse

# Register your models here.
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    change_list_template = 'admin/products_change_list.html'

    actions = ['change_prices_action']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'change_prices/',
                self.admin_site.admin_view(self.change_prices_view),
                name='change_prices'
            ),
        ]
        return custom_urls + urls

    @admin.action(description='Изменить цены')
    def change_prices_action(self, request, queryset):
        if not queryset.exists():
            self.message_user(request, "Не выбрано ни одного товара.", level=message_constants.WARNING)
            return

        ids = ','.join(str(pk) for pk in queryset.values_list('pk', flat=True))
        url = reverse('admin:change_prices') + f'?ids={ids}'
        return HttpResponseRedirect(url)

    def change_prices_view(self, request):
        product_ids = request.GET.get('ids', '').split(',')
        product_ids = [pk for pk in product_ids if pk.isdigit()]
        products = Product.objects.filter(pk__in=product_ids)

        if request.method == 'POST':
            try:
                updated_count = 0
                for product in products:
                    new_price = request.POST.get(f'price_{product.id}')
                    if new_price:
                        product.price = float(new_price)
                        product.save()
                        updated_count += 1

                messages.success(request, f"Цены обновлены для {updated_count} товаров")
                return HttpResponseRedirect(
                    reverse('admin:%s_product_changelist' % self.model._meta.app_label)
                )
            except ValueError:
                messages.error(request, "Ошибка: Некорректное значение цены")

        context = {
            'products': products,
            'opts': self.model._meta,
            'title': 'Изменение цен товаров',
            'changelist_url': reverse('admin:%s_product_changelist' % self.model._meta.app_label)
        }
        return TemplateResponse(
            request,
            'admin/change_price_form.html',
            context
        )