# csc394softwareprojects







#May 11,2017 @ arpan
Steps for creating project virtual env on desktop
  1 . cd desktop
  2.  python3 -m venv csc394project_master (to use python 3)
    ***virtualenv csc394project_master  (folder name) this will use python2.7***
  3. cd csc394project_master/    (ls  will see bin and lib etc) 
  4.  source bin/activate (activate the env)
   ***Looks like this (csc394project_master) Arpans-MacBook-Pro:csc394project_master arpanpatel$*** 

  5. pip freeze (won’t do anything)
  6. pip install django  (it will install Django on virtual env )
      ***Successfully installed django-1.11.1 pytz-2017.2 (end it will say something like this)***
  7.  django-admin.py startproject src (do this it will create src folder inside the project) 
      ***After remove that folder and replace with folder you are trying to export. ***

  8. cd src (folder you created when you start the new project) 
  9. Python3 manage.py runserver ( to run with python 3.. use python3(Mac) or windows (py -3 )  ****might this after trying to   run the server**** ModuleNotFoundError: No module named 'crispy_forms'
  10. pip3 install --user django-crispy-forms (this is does not work for you..)
  11. Press ctrl c or ctrl z 
  12. easy_install -Z django-crispy-forms (to fix crispy forms error when you try to run the server.) ***Successfully           installed django-crispy-forms-1.6.1******Installed /Users/arpanpatel/Desktop/csc394project_master/lib/python3.6/site-         packages/django_crispy_forms-1.6.1-py3.6.egg
  Processing dependencies for django-crispy-forms
  Finished processing dependencies for django-crispy-forms*** (SHOULD SEE SOMETHING LIKE THIS)


  Install django —upgrade ( to update Django to current version)
  pip3 install --user django-crispy-forms (to fix crispy forms error when you try to run the server.) 


#May 6,2017 @arpan 
#Courses have been added in database. 


#May 4,2017 @arpan
#Courses List have been updated on the github. 


