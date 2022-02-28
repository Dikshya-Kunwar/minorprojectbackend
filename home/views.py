from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def login(request):
    return render(request,'home/login.html')

def stream(request):
    return render(request,'home/stream.html')