#Imports de Django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

#Imports locales
from contacts.form import NewContactForm

# Create your views here.
@login_required(login_url='login')
def Index(request):

    return render(request, 'contacts/index.html')

@login_required(login_url='login')
def Add_contact(request):

    if request.method == 'POST':
        form = NewContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewContactForm()

    return render(request, 'contacts/new_contact.html', {'form':form})