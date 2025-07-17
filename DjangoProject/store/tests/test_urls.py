import pytest
from django.urls import reverse, resolve
from store.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView
)

@pytest.mark.django_db
def test_product_list_url():
    path = reverse('product_list')
    resolver_match = resolve(path)
    assert resolver_match.func.view_class == ProductListView

@pytest.mark.django_db
def test_product_detail_url(product):
    path = reverse('product_detail', kwargs={'pk': product.pk})
    resolver_match = resolve(path)
    assert resolver_match.func.view_class == ProductDetailView

@pytest.mark.django_db
def test_product_create_url():
    path = reverse('add')
    resolver_match = resolve(path)
    assert resolver_match.func.view_class == ProductCreateView

@pytest.mark.django_db
def test_product_update_url(product):
    path = reverse('edit_product', kwargs={'pk': product.pk})
    resolver_match = resolve(path)
    assert resolver_match.func.view_class == ProductUpdateView