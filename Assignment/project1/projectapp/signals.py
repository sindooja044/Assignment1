import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel

@receiver(post_save, sender=TestModel)
def post_save_handler(sender, instance, **kwargs):
    print("Signal triggered!")
    time.sleep(5)  # Simulate a delay to demonstrate synchronous behavior
