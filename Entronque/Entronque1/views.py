from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html');
<<<<<<< HEAD
def metodo(request):
    return render(request, 'index.html');
=======

def metodo(request):
    return render(request, 'index1.html');



>>>>>>> origin/master
