from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Index(request):

    return render(request, 'contacts/index.html')

@login_required(login_url='login')
def Add_contact(request):

    return render(request, 'contacts/new_contact.html')