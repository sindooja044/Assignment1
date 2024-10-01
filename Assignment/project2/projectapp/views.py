from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from .models import TestModel
import threading

def test_view(request):
    print(f"View executed in thread: {threading.current_thread().name}")
    TestModel.objects.create(name="Test")
    return HttpResponse("View response after signal execution")
