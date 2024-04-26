from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()