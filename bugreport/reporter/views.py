# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import BugCreateForm,BugUpdateForm
from .models import Bug
from resolver import views as resolverViews
# Create your views here.


def hello_view(request):
    return render(request, 'index.html', {})
    #return HttpResponse("<h1>hi</h1>")
def createBug(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form=BugCreateForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            print form_obj.title
            print form_obj.description
            form_obj.save()
            return HttpResponseRedirect(reverse('viewbugs'))
    else:
        form=BugCreateForm()
        context={"form":form}
    return render(request, 'createBug.html', context)




def updateBug(request,id):
    print("updating bug")
    if request.method == 'POST':
        bug = Bug.objects.get(id=id)
        form=BugUpdateForm(request.POST,instance=bug)
        form_obj=form.save(commit=False)
        form_obj.save()

        return HttpResponseRedirect(reverse('viewbugs'))

    else:
        bug = Bug.objects.get(id=id)
        form=BugUpdateForm(instance = bug)
        context={"form":form}
        return render(request, 'updateBug.html', context)


def viewBugs(request):
    context={}
    allBugs=Bug.objects.all()
    context['bugs']=allBugs
    return render(request,'showBugs.html',context)

def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="reporter").exists():
        return HttpResponseRedirect(reverse('viewbugs'))
    else:
        return HttpResponseRedirect(reverse('resolver_hello_view'))
