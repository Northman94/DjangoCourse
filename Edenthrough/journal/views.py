from django.shortcuts import render
from django.http import HttpResponse


# Creating a View:

def home(request):
    #return HttpResponse("Home Page.")

    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')

