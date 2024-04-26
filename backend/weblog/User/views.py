from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["username"], cd["email"], cd["password"])
            messages.success(request, "successfuly", "success")
            return redirect("home")
    else:
        form = UserRegisterForm()

    return render(request, "signup.html", {"form": form})


def home(request):
    return render(request, "home.html")
