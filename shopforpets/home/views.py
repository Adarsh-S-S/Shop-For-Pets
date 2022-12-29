from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PetProduct
from django.conf import settings
from django.core.mail import send_mail



def index(request):

    if request.method == "POST":
        search=request.POST["msg"]
        data=PetProduct.objects.filter(name__istartswith=search)
    else:
        data=PetProduct.objects.all()


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
        
        elif password=="" or password!=repassword:
            msg="Invalid password"
            return render(request,"register.html",{"b":msg})
        else:
            l1=len(username)
            l2=len(password)
            l3=l1+l2*63513
            l4=str(l3)[:5]
            request.session["his"]=[username,firstname,secondname,email,password,repassword]
            request.session.modified = True
            send_mail("otp validation",f"Your otp is {l4}",settings.EMAIL_HOST_USER,[email,])
            return render(request,"otp.html")
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

def otp(request):

    if request.method == "POST":
        n1=request.POST["n1"]
        n2=request.POST["n2"]
        n3=request.POST["n3"]
        n4=request.POST["n4"]
        n5=request.POST["n5"]
        otp=n1+n2+n3+n4+n5
        li=request.session["his"]
        l1=len(li[0])
        l2=len(li[4])
        l3=l1+l2*63513
        l4=str(l3)[:5]
        if otp==l4:
            user=User.objects.create_user(username=li[0],first_name=li[1],last_name=li[2],email=li[3],password=li[4])
            user.save();
            auth.login(request,user)
            return redirect("/")
        else:
            msg="Otp Is Invalid"
            return render(request,"otp.html",{"msg":msg})
    else:
        return render(request,"otp.html")