from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
def home(request):
    return render(request,'home.html')
def reg(request):
    uname=request.POST['uname']
    email=request.POST['email']
    contact=request.POST['contact']
    address=request.POST['address']
    pwd=request.POST['password']
    p=Person.objects.create_user(username=uname,password=pwd,email=email,contact=contact,address=address)
    p.save()
    messages.success(request,'Successfully Registered')
    return render(request,'login.html')
def log(request):
    uname=request.POST['uname']
    pwd=request.POST['password']
    user=auth.authenticate(username=uname,password=pwd)
    if user is not None:
        data=Person.objects.all()
        return render(request,'table.html',{'data':data})
    else:
        messages.info(request,'Invalid username or password')
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    messages.success(request,'Logged out Successfully')
    return render(request,'login.html')
def test(request):
    return render(request,'test.html')
def delte(request):
    id=request.GET['id']
    Person.objects.get(id=id).delete()
    data=Person.objects.all()
    return render(request,'table.html',{'data':data})
def update(request):
    p=Person()
    p.id=request.POST['iid']
    p.username=request.POST['uname']
    p.email=request.POST['email']
    p.contact=request.POST['contact']
    p.address=request.POST['address']
    p.save()
    data=Person.objects.all()
    return render(request,'table.html',{'data':data})
def search(request):
    uname=request.POST['uname']
    v=Person.objects.get(username=uname)
    return render(request,'table.html',{'data':[p]})

# Create your views here.
