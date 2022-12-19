from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from home.models import PetProduct
from .models import Comment




def detail(request):
    id=request.GET["id"]
    data=PetProduct.objects.get(id=id)
    total=int(data.price)-(int(data.price)*int(data.discount)/100)
    comment=Comment.objects.filter(pro_id=id)
    response=render(request,"detail.html",{"pro":data,"total":total,"comment":comment})
    response.set_cookie("id",data.price)
    return response
    return render(request,"detail.html",{"pro":data,"total":total,"comment":comment})



def cmt(request):
        comment=request.POST["comment"]
        name=request.POST["user"]
        proid=request.POST["id"]
        mt=Comment.objects.create(cmt=comment,name=name,pro_id=proid)
        mt.save();
        return redirect("/product/?id="+proid)