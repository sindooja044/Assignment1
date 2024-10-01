from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from .models import TestModel

def test_view(request):
    TestModel.objects.create(name="Test")
    return HttpResponse("View response after signal execution")
