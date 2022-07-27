from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def hello(response):
    return HttpResponse("hello world")


def message(response):
    return HttpResponse("<h2>i am writting messages</h2>")

def app(request):
    return render(request,"index.html")