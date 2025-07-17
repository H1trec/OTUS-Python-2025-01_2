import pytest
from django.urls import reverse
from store.models import Product, Category

@pytest.fixture
def client():
    from django.test import Client
    return Client()

@pytest.fixture
def category():
    return Category.objects.create(name="Электроника")

@pytest.fixture
def product(category):
    return Product.objects.create(
        name="Смартфон",
        price=29999.99,
        description="Тестовое описание",
        category=category
    )