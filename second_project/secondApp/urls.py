from django.urls import path
from . import views
urlpatterns = [
    path('',views.res),
    path('user/',views.user)
   ]
