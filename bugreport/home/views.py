from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.conf.urls import include, url


@login_required

from django.shortcuts import redirect

def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="reporter").exists():
        # user is an admin
        return redirect(include('reporter.urls'))
    else:
        return redirect(include('reporter.urls'))