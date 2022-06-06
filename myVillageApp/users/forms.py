from dataclasses import field
import email
from pyexpat import model
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:

        model = User

        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),




            # 'status': forms.CheckboxInput(attrs={'class': 'form-control'})

        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:

        model = User

        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'status': forms.CheckboxInput(attrs={'class': 'form-control'})
        }


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
