from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def create_cover(request):
    print("Hello world")
    return HttpResponse("Hello World")
    pass
