"""ContactApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Imports from django
from unicodedata import name
from django.contrib import admin
from django.urls import path

#Imports from local project
from users import views as users

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('welcome/', users.Welcome, name='welcome'),
    path('signup/', users.SingUp, name='signup'),
    path('login/', users.Login, name='login'),
    path('logout/', users.Logout, name='logout'),
    path('index/', users.Index, name='index')
]
