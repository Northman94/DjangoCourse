from django.shortcuts import render
from django.http import HttpResponse


clientList = [

    {
        'id' : '1',
        'name' : 'Chris Mule',
        'profession' : 'Musician',
    },

    {
        'id' : '2',
        'name' : 'Sarah',
        'profession' : 'Carpenter',
    },
]





def register(request):

    return render(request, 'register.html')



def home(request):
    #return HttpResponse("Home Page.")

    context = {'clients' : clientList}

    return render(request, 'index.html', context)

