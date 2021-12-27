from django.urls import path
from authentication_page import views

urlpatterns=[
    path("",views.home,name="home"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("logout",views.logout,name="logout")
    ]