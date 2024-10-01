from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from .models import TestModel
from django.db import transaction

def test_view(request):
    try:
        with transaction.atomic():
            TestModel.objects.create(name="Test")
    except:
        print("Transaction rolled back due to error in signal")
    return HttpResponse("View response after signal execution")
