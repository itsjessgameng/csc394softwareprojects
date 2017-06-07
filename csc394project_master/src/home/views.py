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
	queryset = Student.objects.all()
	
	plan = []
	user = request.user.username
	print(request.FILES)
	if request.method == "POST" and request.POST['action'] == "Submit Info":
		degree = request.POST['major']
		concentration = request.POST['concentration']
		qua = request.POST['quarter']
		numOfCourses = request.POST['numcourses']
		summer = request.POST['summer?']
		student_obj = Student(user = user, degree = degree, concentration = concentration, quarter = qua, numOfCourses = numOfCourses, summer = summer)
		student_obj.save()
		
	elif request.method == "POST" and request.POST['action'] == "Submit":
		some_var = request.POST.getlist('checks[]')
		plan = Algorithm(user, some_var).run()
		print(plan)
		return render(request, "algoOutput.html", {"plan" : plan})
	elif request.method == "POST" and request.POST['action'] == "Change Info":
		Student.objects.filter(user=user).delete()
		return render(request, "profile.html", {"title" : "Profile"})
		
	##elif counter > 0:
	##	if request.POST['action'] == "Submit":
	##		counter = 1
	##	else:
	##		counter = 0
	##		Student.objects.filter(user).delete()
	##		return render(request, "profile.html", context)
	
	context = {
		"title" : "Profile",
		"students" : queryset,
		"plan" : plan,
	}
	
	query = Student.objects.all().filter(user = user)
	if(query.count() > 0):
		queryUser = str(query[0])
	else:
		return render(request, "profile.html", context)
	
	if(queryUser == user):
		return render(request, "EditProfile.html", context)
	else:
		return render(request, "profile.html", context)
	
@login_required(login_url='/login/')
def home_create(request):
	data = json.dumps(plan)
	
	return render(request, "base.html", {'plan':data}) 


def home_update(request):
	return HttpResponse("<h1>Hello from update</h1>")


def home_delete(request):
	return HttpResponse("<h1>Hello from delete</h1>")
	
