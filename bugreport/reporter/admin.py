# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Bug

class BugAdmin(admin.ModelAdmin):
	list_display = ['title', 'createdDate', 'publishedDate' ]
	list_display_links = ["publishedDate"]
	list_filter = ["publishedDate"]
	search_fields = ["title","description"]
	class Meta:
		model = Bug

admin.site.register(Bug,BugAdmin)
