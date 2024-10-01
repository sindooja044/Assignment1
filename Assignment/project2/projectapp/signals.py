import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel

@receiver(post_save, sender=TestModel)
def post_save_handler(sender, instance, **kwargs):
    print(f"Signal triggered in thread: {threading.current_thread().name}")
