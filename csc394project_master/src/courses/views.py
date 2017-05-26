from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Course
from courses.is_models import IS_Course
from django.contrib.contenttypes.models import ContentType

# Create your views here.


def cs_course_list(request):
	#return HttpResponse("<h1>Hello from list</h1>")
	queryset = Course.objects.all()
	context = {
		"object_list": queryset,
		"title" : "Courses"
	}
	return render(request, "cs_Courses.html", context)



def is_course_list(request):
	#return HttpResponse("<h1>Hello from list</h1>")
	queryset =  IS_Course.objects.all()
	context = {
		"object_list": queryset,
		"title" : "Courses"
	}
	return render(request, "is_Courses.html", context)


def cs_course_detail(request, id):
	#return HttpResponse("<h1>Hello from detail</h1>")
	instance = get_object_or_404(Course, id=id)
	context = {
		"title" : instance.course_name,
		"instance": instance
	}
	return render(request, "cs_detail.html", context)

def is_course_detail(request, id):
	#return HttpResponse("<h1>Hello from detail</h1>")
	instance = get_object_or_404(IS_Course, id=id)
	context = {
		"title" : instance.is_course_name,
		"instance": instance
	}
	return render(request, "is_detail.html", context)


	def simulation_list(request):
	#return HttpResponse("<h1>Hello from list</h1>")
		pass 
	




