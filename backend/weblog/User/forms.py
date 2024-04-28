from django import forms
from .models import User
from django.forms import ModelForm


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "password", "email", "image")
        widgets = {
            'password': forms.PasswordInput()
        }


class UserSigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "email", "image")
