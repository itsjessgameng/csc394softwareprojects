
from __future__ import unicode_literals
from django.db import models

class IS_Course(models.Model): 
    is_course_id = models.CharField(max_length=120)
    is_course_name = models.CharField(max_length=120)
    is_pre_req = models.CharField(max_length=120)
    is_quarter_ava = models.CharField(max_length=120)


    

    def __unicode__(self):
        return self.is_course_name

    def __str__(self):
        return self.is_course_name

