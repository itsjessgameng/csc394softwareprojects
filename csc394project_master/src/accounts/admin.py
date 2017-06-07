from __future__ import unicode_literals
from django.contrib import admin

from accounts.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ["degree"]
	list_display_links = ["degree"]
	list_filter = ["degree"]
	search_fields = [" degree"]
	class Metha:
		model = Student

admin.site.register(Student, StudentAdmin) 
