from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
	user = models.CharField(primary_key = True, max_length=100, default=' ')
	degree = models.CharField(max_length=50)
	concentration = models.CharField(max_length=100)
	quarter = models.IntegerField()
	numOfCourses = models.IntegerField()
	summer = models.CharField(max_length=10)
	
	def __unicode__(self):
		return self.user

	def __str__(self):
		return self.user