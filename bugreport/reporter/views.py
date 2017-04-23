# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import BugCreateForm,BugUpdateForm
from .models import Bug

# Create your views here.


def hello_view(request):
    return render(request, 'a.html', {})
    #return HttpResponse("<h1>hi</h1>")
def createBug(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form=BugCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})
    else:
        form=BugCreateForm()
        context={"form":form}
    return render(request, 'createBug.html', context)

def updateBug(request):
    if request.method == 'POST':
        form=BugUpdateForm(request.POST)
        if form.is_valid():
            print(form.bugId)
            bug=Bug().objects.get(bugId=form.bugId)
            bug.description=form.description
            bug.title=form.title
            bug.save()
            #replace this with proper page
            return render(request,'showBugs.html',context)
        else:
            return render(request,'createBug.html',context)
    else:
        form=BugUpdateForm()
        context={"form":form}
        return render(request,'createBug.html',context)


def viewBugs(request):
    context={}
    allBugs=Bug.objects.all()
    context['bugs']=allBugs
    return render(request,'showBugs.html',context)
