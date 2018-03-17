"""Defines URL patterns for employee."""
from django.conf.urls import url
from . import views

app_name='employee'

urlpatterns = [
    # Home page
    url(r'^employee/$', views.add_emp_page, name='add_emp_page'),
    url(r'^employee/viewemployees/$', views.index, name='index'),
    url(r'^employee/edit employee/(?P<id>[0-9]+)/$', views.add_emp_page, name='add_emp_page'),
    url(r'^employee/create employee/$', views.create_emp, name='create_emp'),
    url(r'^employee/delete employee/(?P<id>[0-9]+)/$', views.delete_emp, name='delete_emp'),
    url(r'^employee/update employee/$', views.update_emp, name='update_emp'),


]
