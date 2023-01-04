from django.shortcuts import render,HttpResponse
from django.db import IntegrityError
from Home.models import student
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
 return render(request,'about.html')

def registration(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        regno = request.POST.get('regno')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        committee = request.POST.get('committee')
        skills = request.POST.get('skills')
        nativeplace = request.POST.get('nativeplace')
        volunteers=student(firstname=firstname,lastname=lastname,
        regno=regno,mobile=mobile,email=email,committee=committee,nativeplace=nativeplace,
        skills=skills,date=datetime.today())
        volunteers.save()
    return render(request,'registration.html')
 
def committees(request):
 return render(request,'committees.html')