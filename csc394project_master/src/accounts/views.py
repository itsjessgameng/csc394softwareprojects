from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login, 
	logout,

	)
	
from .models import Student
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.

def login_view(request):
	print(request.user.is_authenticated())
	next = request.GET.get('next')
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)
		print(request.user.is_authenticated())
		#redirect


	return render(request, "forms.html", {"form":form, "title":title})


def register_view(request):
	title = "Register"
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

	return render(request, "forms.html", {"form":form, "title":title})


def logout_view(request):
	title = "Logout"
	logout(request)

	return HttpResponseRedirect('/login/?next=/home/')
	
def get_student_list(request):
	queryset = Student.objects.all()
	context = {
		"student_list": queryset,
		"title" : "Students"
	}
	return render(request, "staff_form.html", context)

def student_detail(request, user):	
	#return HttpResponse("<h1>Hello from detail</h1>")
	instance = get_object_or_404(Student, user=user)
	context = {
		"title" : instance.degree,
		"instance": instance
		
	}
	
	##if request.method == "POST" and request.POST['action'] == "Submit Info":
	##return render(request, "EditProfile.html", context)
	##else:
	return render(request, "student_detail.html", context)
	