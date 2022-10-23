from django.shortcuts import render
from django.http import HttpResponse


# Creating a View:

def home(request):
    #return HttpResponse("Home Page.")

    first_name = "Luke Paul"

    context = {'name':first_name}

    return render(request, 'index.html', context)


def register(request):
    return render(request, 'register.html')

