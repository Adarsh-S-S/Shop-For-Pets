from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from home.models import PetProduct
from .models import Comment
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail




def detail(request):
    id=request.GET["id"]
    data=PetProduct.objects.get(id=id)
    total=int(data.price)-(int(data.price)*int(data.discount)/100)
    comment=Comment.objects.filter(pro_id=id)
    if "his" in request.session:
        if id in request.session["his"]:
            request.session["his"].remove(id)
            request.session["his"].insert(0,id)
        else:
            request.session["his"].insert(0,id)
        if len(request.session["his"])>4:
            request.session["his"].pop()
        print(request.session["his"])
        recent=PetProduct.objects.filter(id__in=request.session["his"])
        print(recent)
        request.session.modified=True
        return render(request,"detail.html",{"pro":data,"total":total,"comment":comment,"recent":recent})

    else:
        print("Hello")
        request.session["his"]=[id]
        print(request.session["his"])
        return render(request,"detail.html",{"pro":data,"total":total,"comment":comment})

def cmt(request):
        comment=request.POST["comment"]
        name=request.POST["user"]
        proid=request.POST["id"]
        mt=Comment.objects.create(cmt=comment,name=name,pro_id=proid)
        mt.save();
        return redirect("/product/?id="+proid)





def detail2(request):
    id=request.GET["id"]
    if cache.get(id):
        print("Data from cache")
        data=cache.get(id)
    else:
        data=PetProduct.objects.get(id=id)
        print("Data From DataBase")
        cache.set(id,data)

    total=int(data.price)-(int(data.price)*int(data.discount)/100)
    comment=Comment.objects.filter(pro_id=id)
    return render(request,"detail.html",{"pro":data,"total":total,"comment":comment})




def email(request):
    email_from =  settings.EMAIL_HOST_USER
    email_to = ["adhuzz123@gmail.com",]
    subject = "Testing The Process"
    message = "If you recieve this mail then it is working."
    send_mail(subject,message,email_from,email_to)
    return render(request,"test.html")
