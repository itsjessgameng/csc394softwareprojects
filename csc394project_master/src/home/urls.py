from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
#home
from .views import home_, home_create, home_list, home_detail, home_update, home_delete
from accounts.views import login_view, register_view, logout_view
from courses.views import course_list, course_detail
urlpatterns = [
    
    url(r'^home/', home_), # profile?
    url(r'^create/', home_create), #

    # url(r'^list/', course_list),
    # url(r'^detail/(?P<id>\d+)/$', home_detail, name='detail'),

    url(r'^update/', home_update),
    url(r'^delete/', home_delete),
    ##### auth

    url(r'^login/', login_view, name='login'),
    url(r'^register/', register_view, name='register'),
    url(r'^logout/', logout_view, name='logout'),
    #### crriculum
    
    url(r'^list/', course_list),
    url(r'^detail/(?P<id>\d+)/$', course_detail, name='detail'),



    
]
