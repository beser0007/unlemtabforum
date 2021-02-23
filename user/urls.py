from django.contrib import admin
from django.urls import path
from user import views


urlpatterns = [
    path("login/",views.loginUser,name="login"),
    path("register/",views.register,name="register"),
    path("logout/",views.logoutUser,name="logout"),
]