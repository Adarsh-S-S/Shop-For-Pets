from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PetProduct



def index(request):
    data=PetProduct.objects.all()
    if "pas" in request.COOKIES and "id" in request.COOKIES:
        cook=request.COOKIES["pas"]
        price=request.COOKIES["id"]
        return render(request,"index.html",{"abc":cook,"pro":data,"id":price})
    else:
        return render(request,"index.html",{"pro":data})

def register(request):
    if request.method=="POST":
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
    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["pass"]
        check=auth.authenticate(username=username,password=password)
        if check is not None:
            auth.login(request,check)
            response=redirect("/")
            response.set_cookie("pas",password)
            return response                               
        else:
            msg="Invalid Username or password"
            return render(request,"login.html",{"c":msg})
    else:    
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    response=redirect("/")
    response.delete_cookie("pas")
    response.delete_cookie("id")
    return response

    
    
      
    




