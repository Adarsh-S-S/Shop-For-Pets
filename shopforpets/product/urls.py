from django.urls import path
from . import views



urlpatterns = [
     path("",views.detail2,name="detail"),
     path("cmt/",views.cmt,name="cmt")
]