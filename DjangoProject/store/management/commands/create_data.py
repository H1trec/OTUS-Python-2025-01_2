from django.core.management.base import BaseCommand
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Create test data'

    def handle(self, *args, **options):
        cat1 = Category.objects.create(name="Electronics", description="All electronic goods")
        cat2 = Category.objects.create(name="Furniture", description="Home furniture items")

        Product.objects.create(category=cat1, name="Laptop", description="Powerful laptop for programming",
                               price=1200.00)
        Product.objects.create(category=cat2, name="Chair", description="Comfortable office chair", price=70.00)

        print("Test data created successfully!")