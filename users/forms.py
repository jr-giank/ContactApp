#Django's imports 
from turtle import color
from django import forms
from django.core.exceptions import ValidationError

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
        max_length=40,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )

class SignUpForm(forms.Form):

    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
    

    first_name = forms.CharField(
        label=False,
        max_length=45,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Names'
            }
        )
    )

    last_name = forms.CharField(
        label=False,
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Last Names'
            }
        )
    )

    username = forms.CharField(
        label=False,
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Username'
            }
        )
    )

    password = forms.CharField(
        label=False,
        max_length=15,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Password',
            }
        ),
        error_messages= {'class': 'text-white'}
    )

    password_confirmation = forms.CharField(
        label=False,
        max_length=15,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Password Confirmation',
            }
        ),
        error_messages= {'class': 'text-white'}
    )

    email = forms.CharField(
        label=False,
        max_length=40,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Email'
            }
        )
    )

    def clean_username(self):

        username = self.cleaned_data['username']

        user_exists = User.objects.filter(username=username).exists()

        if user_exists == True:
            raise ValidationError("Username is already taken")

        return username

    def clean(self):

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise ValidationError('Password does not match')

        return data

    def save(self):

        data = self.cleaned_data

        data.pop('password_confirmation')

        new_user = User.objects.create_user(**data)