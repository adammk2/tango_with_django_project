from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!<br><a href='https://www.pictureofhotdog.com'>LINK!</a>")

def about(request):
    return HttpResponse("Rango says here is the about page.<br><a href='../'>PLS GO BACK</a>")