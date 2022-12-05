from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User



def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["pass"]
        check=auth.authenticate(username=username,password=password)
        if check is not None:
            auth.login(request,check)
            return redirect("/")
        else:
            msg="Invalid Username and password"
            return render(request,"login.html",{"c":msg})
    else:    
        return render(request,"login.html")


def reg(request):
    username=request.POST["uname"]
    firstname=request.POST["fname"]
    secondname=request.POST["sname"]
    email=request.POST["email"]
    password=request.POST["pname"]
    repassword=request.POST["rpname"]
    ucheck=User.objects.filter(username=username)
    echeck=User.objects.filter(email=email)
    if ucheck:
        msg="Username Exits"
        return render(request,"register.html",{"b":msg})
    elif echeck:
        msg="Email Exits"
        return render(request,"register.html",{"b":msg})
    elif password=="" or password!=repassword:
        msg="Invalid password"
        return render(request,"register.html",{"b":msg})
    else:
        user=User.objects.create_user(username=username,first_name=firstname,last_name=secondname,email=email,password=password)
        user.save();
        return redirect("/")


    
    
      
    




