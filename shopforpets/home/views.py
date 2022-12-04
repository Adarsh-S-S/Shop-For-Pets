from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User



def index(request):
    return render(request,"index.html")


def test(request):
    val="Java"
    val2=" and object oriented programming"
    return render(request,"test.html",{"a":val,"b":val2})

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def snd(request):
    username=request.GET["uname"]
    password=request.GET["pass"]
    check=auth.authenticate(username=username,password=password)
    if check is not None:
        auth.login(request,check)
        return redirect("/")
    else:
        msg="Invalid Username and password"
        return render(request,"test.html",{"c":msg})


def reg(request):
    username=request.GET["uname"]
    firstname=request.GET["fname"]
    secondname=request.GET["sname"]
    email=request.GET["email"]
    password=request.GET["pname"]
    repassword=request.GET["rpname"]
    ucheck=User.objects.filter(username=username)
    echeck=User.objects.filter(email=email)
    if ucheck:
        msg="Username Exits"
        return render(request,"test.html",{"b":msg})
    elif echeck:
        msg="Email Exits"
        return render(request,"test.html",{"b":msg})
    elif password=="" or password!=repassword:
        msg="Invalid password"
        return render(request,"test.html",{"b":msg})
    else:
        user=User.objects.create_user(username=username,first_name=firstname,last_name=secondname,email=email,password=password)
        user.save();
        return redirect("/")


    
    
      
    




