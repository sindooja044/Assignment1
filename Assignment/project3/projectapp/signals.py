from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel
from django.db import transaction

@receiver(post_save, sender=TestModel)
def post_save_handler(sender, instance, **kwargs):
    print("Signal triggered!")
    raise Exception("Error in signal handler")  # Raise an error to test rollback
