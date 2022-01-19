from django.shortcuts import render

# Create your views here.
def SingUp(request):

    return render(request, 'users/signup.html')