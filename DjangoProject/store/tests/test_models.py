import pytest
from django.core.exceptions import ValidationError
from store.models import Product


@pytest.mark.django_db
def test_product_creation(product):
    assert product.name == "Смартфон"
    assert product.price == 29999.99
    assert str(product) == f"{product.name} ({product.category.name})"

@pytest.mark.django_db
def test_product_update(product):
    product.name = "Ноутбук"
    product.save()
    updated = Product.objects.get(pk=product.pk)
    assert updated.name == "Ноутбук"

@pytest.mark.django_db
def test_product_deletion(product):
    product_id = product.id
    product.delete()
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(pk=product_id)

@pytest.mark.django_db
def test_price_validation():
    with pytest.raises(ValidationError):
        p = Product(name="Тест", price=-100)
        p.full_clean()