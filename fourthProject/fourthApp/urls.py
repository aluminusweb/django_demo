from django.contrib import admin
from django.urls import path
from fourthApp import views
app_name='fourthApp'

urlpatterns = [
    path('',views.index , name='index'),
    path('other/',views.other ,name='other'),
    path('relative/', views.relative_url_template, name='relative'),
  ]
