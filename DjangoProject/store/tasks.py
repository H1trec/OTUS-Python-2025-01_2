from celery import shared_task
import logging
import time

logger = logging.getLogger(__name__)

@shared_task
def log_product_add(product_id):
    from store.models import Product
    product = Product.objects.get(id=product_id)
    print(f"New product added: {product.name}")
    time.sleep(5)  # Имитация долгой задачи
    return f"Logged product {product.id}"