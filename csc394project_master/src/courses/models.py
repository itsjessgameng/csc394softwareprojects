from __future__ import unicode_literals
from django.db import models

# this CS Model
class Course(models.Model): 
    course_id = models.CharField(max_length=120)
    course_name = models.CharField(max_length=120)
    pre_req = models.CharField(max_length=120)
    cs_cons = models.CharField(max_length=120)
    cs_class_type = models.CharField(max_length=120)


    fall = models.BooleanField()
    winter = models.BooleanField()
    spring = models.BooleanField()
    summer = models.BooleanField()
    online = models.BooleanField()



    


    def __unicode__(self):
        return self.course_name

    def __str__(self):
        return self.course_name

