from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


# Create your views here.
def index(request):
    us=User.objects.all()
    return render(request,'index.html',{'us':us})

def userreg(request):
    return render(request, "userreg.html",)

def insertuser(request):
    vuid=request.POST['tuid']
    vuname=request.POST['tuname']
    vuemail=request.POST['tuemail']
    vucontact=request.POST['tucontact']
    us=User(uid=vuid,uname=vuname,uemail=vuemail,ucontact=vucontact)
    us.save()
    return redirect("/")

def update(request,uid):
    us=User.objects.get(uid=uid)
    return render(request,'update.html',{'us':us})

def delete(request,uid):
    us=User.objects.get(uid=uid)
    us.delete()
    return redirect("/")

def uprec(request,uid):
    vuid=request.POST['tuid']
    vuname=request.POST['tuname']
    vuemail=request.POST['tuemail']
    vucontact=request.POST['tucontact']
    us=User.objects.get(uid=uid)
    us.uid=vuid
    us.uname=vuname
    us.uemail=vuemail
    us.ucontact=vucontact
    us.save()
    return redirect("/")
