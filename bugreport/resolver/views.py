# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from reporter.models import Bug


# Create your views here.


def hello_view(request):
	context={}
	allBugs=Bug.objects.all()
	context['bugs']=allBugs
	return render(request,'dashboard.html',context)


def solveBug(request):
    # If this is a POST request then process the Form data

    return render(request, 'a.html', {})

def assignBug(request):

    return render(request,'a.html',{})


def deleteBug(request, id):
	bug = Bug.objects.get(id=id)
	bug.delete()
	return HttpResponseRedirect(reverse('resolver_hello_view'))
