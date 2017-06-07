# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from courses.models import Course

from courses.is_models import IS_Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ["course_id","course_name","pre_req", "cs_cons", "cs_class_type" , "fall", "winter", "spring", "summer", "online"]
	list_display_links = ["is_course_id"] 
	list_display_links = ["course_id"]
	list_filter = ["course_id"]
	search_fields = [" course_id", " course_name"]
	class Metha:
		model = Course

admin.site.register(Course, CourseAdmin) 


class IS_CourseAdmin(admin.ModelAdmin):
	list_display = ["is_course_id","is_course_name","is_pre_req", "is_cons", "is_class_type" ,"fall", "winter", "spring", "summer", "online"]
	list_display_links = ["is_course_id"]
	list_filter = ["is_course_id"]
	search_fields = [" is_course_id", " is_course_name"]
	class Metha:
		model =  IS_Course

admin.site.register(IS_Course, IS_CourseAdmin)