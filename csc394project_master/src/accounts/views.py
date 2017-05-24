from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login, 
	logout,

	)
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
	form = UserRegisterForm(request.POST or None)

	return render(request, "forms.html", {"form":form, "title":title})


def logout_view(request):
	title = "Logout"
	logout(request)

	return HttpResponseRedirect('/login/?next=/home/')
	