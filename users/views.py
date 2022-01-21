from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from users.forms import LoginForm

def Welcome(request):

    return render(request, 'users/welcome.html')

def SingUp(request):

    return render(request, 'users/signup.html')

def Login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'users/login.html', {'form':form, 'error':'Username or password incorrect'})                      
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form':form})

@login_required
def Logout(request):
    logout(request)

    return redirect('login')

def Index(request):

    return render(request, 'contacts/index.html')
