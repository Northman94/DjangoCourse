from django.shortcuts import render
from django.http import HttpResponse


# Creating a View:

def home(request):
    return HttpResponse("Home Page.")


def register(request):
    return HttpResponse("Welcome to Registration Page.")

