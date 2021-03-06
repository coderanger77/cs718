# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import uuid



class Bug(models.Model):
    #bug-->title,description,files,tags,bugid
    #files not taken care  as of now. will include once basic is done.
    title = models.CharField(max_length=200,default="name..")
    image = models.FileField(null=True, blank=True)
    description = models.TextField(default="some description here..")
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
