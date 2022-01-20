from urllib import request
from django.shortcuts import render

# Create your views here.

def Welcome(request):

    return render(request, 'users/welcome.html')

def SingUp(request):

    return render(request, 'users/signup.html')

def Login(request):

    return render(request, 'users/login.html')