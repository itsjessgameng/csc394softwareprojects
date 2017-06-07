# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from .models import Home
from accounts.models import Student
from django.contrib.contenttypes.models import ContentType
from home.algorithm import Algorithm
# from home.algorithm import Simulation
import json 
# Create your views here.

@login_required(login_url='/login/')
def home_(request):
	# return HttpResponse("<h1>Hello from home</h1>")
	context = {
		"title" : "Profile",
		
	}
	plan = []
	user = request.user.username
	if request.method == "POST":
		degree = request.POST['major']
		concentration = request.POST['concentration']
		qua = request.POST['quarter']
		numOfCourses = request.POST['numcourses']
		summer = request.POST['summer?']
		student_obj = Student(user = user, degree = degree, concentration = concentration, quarter = qua, numOfCourses = numOfCourses, summer = summer)
		student_obj.save()
		plan = Algorithm(user).run()
	
	

	return render(request, "profile.html", {'plan':plan})
	
@login_required(login_url='/login/')
def home_create(request):
	data = json.dumps(plan)
	
	return render(request, "base.html", {'plan':data}) 


def home_update(request):
	return HttpResponse("<h1>Hello from update</h1>")


def home_delete(request):
	return HttpResponse("<h1>Hello from delete</h1>")
	
