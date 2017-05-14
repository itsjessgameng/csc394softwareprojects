from __future__ import unicode_literals
from django.db import models


class Course(models.Model): 
    course_id = models.CharField(max_length=120)
    course_name = models.CharField(max_length=120)
    pre_req = models.CharField(max_length=120)
    quarter_ava = models.CharField(max_length=120)






    


    def __unicode__(self):
        return self.course_name

    def __str__(self):
        return self.course_name

