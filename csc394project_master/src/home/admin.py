# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from home.models import Home

class HomeAdmin(admin.ModelAdmin):
	list_display = ["title","updated", "timestamp"]
	list_display_links = ["updated"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content"]
	class Metha:
		model = Home

admin.site.register(Home, HomeAdmin) 
