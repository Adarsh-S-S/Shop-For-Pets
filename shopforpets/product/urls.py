from django.urls import path
from . import views



urlpatterns = [
     path("",views.detail2,name="detail"),
     path("cmt/",views.cmt,name="cmt"),
     path("email/",views.email,name="emailpage"),
     path("search/",views.search,name="searchpage"),
     path("auto/",views.autosearch,name="autopage")

]