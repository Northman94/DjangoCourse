from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    #return HttpResponse("Home Page.")

    return render(request, 'index.html')

