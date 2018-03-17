"""Defines URL patterns for pizzas."""
from django.conf.urls import url
from . import views
app_name='pizzas'
urlpatterns = [
# Home page
url(r'^$', views.index, name='index'),
url(r'^pizza/$', views.pizzas, name='pizzas'),
url(r'^toppings/(?P<idv>[0-9]+)/$', views.toppings, name = 'toppings')
        ]
