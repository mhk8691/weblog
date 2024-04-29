from django import forms
from .models import Post
from django.forms import ModelForm


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','image')