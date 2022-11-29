from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")


def test(request):
    val="Java"
    val2=" and object oriented programming"
    return render(request,"test.html",{"a":val,"b":val2})




