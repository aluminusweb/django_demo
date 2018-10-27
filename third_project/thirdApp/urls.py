
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('Form_Name/',views.form_name),
   ]
