#Django's imports 
from django import forms

#
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    username = forms.CharField(
        label=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )

    password = forms.CharField(
        label=False,
        max_length=25,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )