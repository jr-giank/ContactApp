#Imports de Django
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

#Imports locales
from contacts.form import NewContactForm
from contacts.models import Contact
#from datetime import datetime as dt

# Create your views here.
@login_required(login_url='login')
def Index(request):

    return render(request, 'contacts/index.html')

@login_required(login_url='login')
def Add_contact(request):

    if request.method == 'POST':
        form = NewContactForm(request.POST)

        if form.is_valid():
            contact = Contact.objects.create()
            contact.name = request.POST['name']
            contact.last_name = request.POST['last_name']
            contact.telephone_number = request.POST['telephone_number']
            contact.user = request.user
            contact.save()
            return redirect('index')
    else:
        form = NewContactForm()

    return render(request, 'contacts/new_contact.html', {'form':form})

@login_required(login_url='login')
def All_contacts(request):

    user = request.user

    contacts = Contact.objects.filter(user=user)

    return render(request, 'contacts/all_contacts.html', {'contacts':contacts})

@login_required(login_url='login')
def Modified_contacts(request, pk):

    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        form = NewContactForm(request.POST)
        
        if form.is_valid():
            contact.name = request.POST['name']
            contact.last_name = request.POST['last_name']
            contact.telephone_number = request.POST['telephone_number']
            contact.save()
            return redirect('contacts')
    else:
        form = NewContactForm(initial={'name':contact.name, 'last_name':contact.last_name, 'telephone_number':contact.telephone_number})


    return render(request, 'contacts/modified_contact.html', {'form':form, 'contact':contact})

@login_required(login_url='login')
def Delete_contact(request, pk):

    contact = Contact.objects.get(id=pk)
    contact.delete()

    user = request.user
    contacts = Contact.objects.filter(user=user)

    return render(request, 'contacts/all_contacts.html', {'contacts':contacts})