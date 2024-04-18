from django.shortcuts import render
from django.http import HttpResponse

def todo(request):
    print("Inside todo view function")
    return HttpResponse("Hello, Hina!")
