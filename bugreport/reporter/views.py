# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import BugCreateForm

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
        form=BugUpdateForm(requeset.POST)
        #if form.is_valid():
    else:
        form=BugUpdateForm()
        context={"form":form}
    return render(request,'createBug.html',context)
