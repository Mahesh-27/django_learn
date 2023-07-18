from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms 


class newtaskform(forms.Form):
      task=forms.CharField(label="New Task")

tasks=[]
def index(request):
    
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"tasks/index.html",{
        "tasks":request.session["tasks"]
    })
     
def add(request):
    if request.method=="POST":
        form=newtaskform(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "form":form
                })
    return render(request,"tasks/add.html",{
        "form":newtaskform()
    })