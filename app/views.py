from django.shortcuts import render
from .models import Sender
# Create your views here.

def index(request):
    if request.method=="POST":
        t = request.POST['toUser']
        s = request.POST['sub']
        m = request.POST['msg']
        Sender.objects.create(to=t,sub=s,msg=m)     
    return render(request,'index.html')


def user1(request):
    sender = Sender.objects.all()
    return render(request,'user1.html',{'sender':sender})

def user2(request):
    sender = Sender.objects.all()
    return render(request,'user2.html',{'sender':sender})

def user3(request):
    sender = Sender.objects.all()
    return render(request,'user3.html',{'sender':sender})

def sent(request):
    sender = Sender.objects.all()
    return render(request,'sent.html',{'sender':sender})