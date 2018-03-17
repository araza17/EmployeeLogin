
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
app_name='user'


urlpatterns = [
    url(r'^user/$', views.index, name='index'),
    url(r'^user/register/$', views.register, name='register'),
    url(r'^order/', views.order, name='order'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    
]
