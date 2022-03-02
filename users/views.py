from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'E-Mail Taken')
                 return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect('login')    
    else:
        return render(request,'users/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user =auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'users/login.html')