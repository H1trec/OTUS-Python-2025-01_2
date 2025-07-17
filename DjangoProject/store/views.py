from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from .tasks import log_product_add

class ProductListView(ListView):
    model = Product
    template_name = 'list.html'  # Сохраняем ваш текущий шаблон
    context_object_name = 'object_list'  # Для совместимости со старым кодом


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'  # Сохраняем ваш текущий шаблон


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add.html'  # Используем существующий шаблон
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        """Вызывается при валидной форме"""
        response = super().form_valid(form)  # Стандартное сохранение объекта

        # Асинхронный вызов Celery-задачи
        log_product_add.delay(self.object.id)  # self.object - созданный товар

        return response

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit.html'  # Используем существующий шаблон
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'  # Новый шаблон
    success_url = reverse_lazy('product_list')


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('category_list')  # Убедитесь, что у вас есть этот URL


def base_view(request):
    """ Основная страница (оставляем как функцию, если она простая) """
    return render(request, 'base.html')