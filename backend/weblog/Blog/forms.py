from django import forms
from .models import Post
from django.forms import ModelForm
from Categories.models import Category

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "image", "categories")

class UpdatePost(forms.ModelForm):

    class Meta:
        model = Post
        # fields = ("title", "content", "image", "categories.name")
        fields = ("title", "content", "image", "categories")
