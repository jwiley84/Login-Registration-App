from django.conf.urls import url
from . import views     #(imports views.py of the current folder)

urlpatterns = [ 
    url(r'^$', views.index) 
    ]