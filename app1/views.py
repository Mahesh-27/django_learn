
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"app1\index.html")

def greet(request,name):
    return render(request,"app1/greet.html",{
        "name":name.capitalize()
    })

def j(request):
    return HttpResponse("HEllo, J!!!")

def brain(request):
    return HttpResponse("HEllo, brain!!!")

def david(request):
    return HttpResponse("HEllo, david!!!")

