"""bugreport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
<<<<<<< HEAD
from .views import hello_view,createBug,updateBug,viewBugs


urlpatterns = [
    url(r'^$', hello_view, name='hello_view'),
    url(r'^createBug$',createBug),
=======
from .views import hello_view,createBug,updateBug,viewBugs,login_success
urlpatterns = [
    # url(r'^$', hello_view),
    url(r'^$', login_success,name='home'),
    url(r'^createBug$',createBug,name="createBug"),
>>>>>>> 6c4fe980a8183b9763eeae76a5761c5527fd1d4d
    url(r'^updateBug/(?P<id>[0-9]+)/$',updateBug,name='update'),
    url(r'^viewBugs$',viewBugs,name='viewbugs'),
]
