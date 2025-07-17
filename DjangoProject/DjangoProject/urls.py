from django.contrib import admin
from django.urls import path
from store.views import (
    base_view,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/edit_price', ProductListView.as_view(), name='product_list'),  # Изменено на CBV
    path('', base_view, name='home'),
    
    # Товары (CBV)
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),  # Новый URL для удаления
    path('add/', ProductCreateView.as_view(), name='add'),
    
    # Категории
    path('add_category/', CategoryCreateView.as_view(), name='add_category'),
]