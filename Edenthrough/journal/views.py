from django.shortcuts import render
from django.http import HttpResponse

from . models import Task


def home(request):
    #return HttpResponse("Home Page.")

    return render(request, 'index.html')


def task(request):

    # - Return All the records from Task database table/model
    # queryAllData = Task.objects.all()
    queryData = Task.objects.get(title="Complete Spreadsheet")

    context = {'task': queryData}


    return render(request, 'task.html', context)


 