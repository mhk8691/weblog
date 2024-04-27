from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserSigninForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .models import User


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username_list = User.objects.filter(username=cd["username"]).first()
            if not username_list:

                User.objects.create(
                    username=cd["username"],
                    email=cd["email"],
                    password=cd["password"],
                    type="0",
                )
                messages.success(request, "Your registration was successful", "success")
                return redirect("home")
            else:
                messages.error(
                    request, "The username was chosen by someone else", "danger"
                )
    else:
        form = UserRegisterForm()

    return render(request, "signup.html", {"form": form})


def home(request):
    username = request.COOKIES.get("user", None)
    print(username)
    return render(request, "home.html", {"username": username})


def signin(request):
    if request.method == "POST":
        form = UserSigninForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.filter(
                username=cd["username"], password=cd["password"]
            ).first()
            if user is not None:
                messages.success(request, "Your login was successful", "success")
                response = HttpResponseRedirect("/")
                response.set_cookie("user", cd["username"])
                print(response)
                return response
            else:
                messages.error(
                    request, "The username or password is incorrect", "danger"
                )

    else:
        form = UserSigninForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    response = HttpResponseRedirect("/")
    response.delete_cookie("user")
    return response
