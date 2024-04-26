from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserSigninForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["username"], cd["email"], cd["password"])
            messages.success(request, "Your registration was successful", "success")
            return redirect("home")
    else:
        form = UserRegisterForm()

    return render(request, "signup.html", {"form": form})


def home(request):
    return render(request, "home.html")


def signin(request):
    if request.method == "POST":
        form = UserSigninForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, "Your login was successful", "success")
                return redirect("home")
            else:
                messages.error(
                    request, "The username or password is incorrect", "danger"
                )

    else:
        form = UserSigninForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")
