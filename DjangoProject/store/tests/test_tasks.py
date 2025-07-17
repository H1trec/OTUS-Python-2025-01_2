from django.test import TestCase
from store.tasks import log_product_add
from store.models import Product

class CeleryTasksTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(name="Test", price=100)

    def test_log_task(self):
        # Проверка синхронного выполнения
        result = log_product_add(self.product.id)
        self.assertIsNone(result)  # Для @shared_task без return

    def test_async_task(self):
        # Проверка асинхронного вызова
        task = log_product_add.delay(self.product.id)
        self.assertEqual(task.status, 'SUCCESS')