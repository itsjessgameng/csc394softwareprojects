# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from .models import Home 
from django.contrib.contenttypes.models import ContentType

# Create your views here.

@login_required(login_url='/login/')
def home_(request):
	# return HttpResponse("<h1>Hello from home</h1>")
	context = {
		"title" : "Profile"

	}
	return render(request, "profile.html", context)


def home_list(request):
	#return HttpResponse("<h1>Hello from list</h1>")
	queryset = Home.objects.all()
	context = {
		"object_list": queryset,
		"title" : "List"
	}
	return render(request, "index.html", context)


def home_create(request):
	return HttpResponse("<h1>Hello from create</h1>")


def home_detail(request, id):
	#return HttpResponse("<h1>Hello from detail</h1>")
	instance = get_object_or_404(Home, id=id)
	context = {
		"title" : instance.title,
		"instance": instance
	}
	return render(request, "home_detail.html", context)


def home_update(request):
	return HttpResponse("<h1>Hello from update</h1>")


def home_delete(request):
	return HttpResponse("<h1>Hello from delete</h1>")
