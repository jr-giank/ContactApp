#Imports de Django
from django import forms

#Import locales
from contacts.models import Contact

class NewContactForm(forms.Form):
    
    name = forms.CharField(
        min_length=5,
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center',
            }
        )
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center'
            }
        )
    )

    telephone_number = forms.CharField(
        min_length=10,
        max_length=10,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control text-center'
            }
        )
    )

    def clean(self):

        data = super().clean()

        return data

    def save(self):

        data = self.cleaned_data

        new_contact = Contact.objects.create(**data)

