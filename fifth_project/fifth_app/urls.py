from django.contrib import admin
from django.urls import path
from fifth_app import views

app_name='fifth_app'
urlpatterns = [
    path("",views.index,name='index'),
    path("register/",views.register,name='register'),
    path("logout/",views.user_logout,name='logout'),
    path("login/",views.user_login,name='login'),
    path('admin/', admin.site.urls),
]
