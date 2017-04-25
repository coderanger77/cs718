# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def hello_view(request):
    return render(request, 'a.html', {})
    #return HttpResponse("<h1>hi</h1>")

def solveBug(request):
    # If this is a POST request then process the Form data
    
    return render(request, 'a.html', context)

def assignBug(request):
    
    return render(request,'a.html',context)
