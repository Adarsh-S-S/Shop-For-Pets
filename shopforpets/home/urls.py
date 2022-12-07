from django.urls import path
from . import views



urlpatterns = [
    path("",views.index,name="homepage"),
    path("register/",views.register,name="registerpage"),
    path("login/",views.login,name="loginpage"),
    path("logout/",views.logout,name="logout")
]