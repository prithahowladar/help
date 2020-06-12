from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('count/',views.count, name = "count"),
    path('35/',views.msg, name = "35"),
    path('flow/',views.flow, name = 'flow')

]