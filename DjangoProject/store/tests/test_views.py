import pytest
from django.urls import reverse
from store.models import Product

@pytest.mark.django_db
def test_product_list_view(client, product):
    url = reverse('product_list')
    response = client.get(url)
    assert response.status_code == 200
    assert b"Смартфон" in response.content

@pytest.mark.django_db
def test_product_detail_view(client, product):
    url = reverse('product_detail', kwargs={'pk': product.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert str(product.price).encode() in response.content

@pytest.mark.django_db
def test_product_create_view(client):
    url = reverse('add')
    data = {
        'name': 'Новый товар',
        'price': 1000,
        'description': 'Тест'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Product.objects.filter(name="Новый товар").exists()

@pytest.mark.django_db
def test_product_update_view(client, product):
    url = reverse('edit_product', kwargs={'pk': product.pk})
    data = {'name': 'Обновленный', 'price': 2000}
    response = client.post(url, data)
    assert response.status_code == 302
    updated = Product.objects.get(pk=product.pk)
    assert updated.name == "Обновленный"