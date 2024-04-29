from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserSigninForm, UserEditForm
from django.contrib import messages
from .models import User
from Blog.models import Post


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data

            username_list = User.objects.filter(username=cd["username"]).first()
            if not username_list:

                User.objects.create(
                    username=cd["username"],
                    email=cd["email"],
                    password=cd["password"],
                    type="0",
                    image=cd["image"],
                )
                messages.success(request, "Your registration was successful", "success")
                return redirect("signin")
            else:
                messages.error(
                    request, "The username was chosen by someone else", "danger"
                )
    else:
        form = UserRegisterForm()

    return render(request, "signup.html", {"form": form})

from django.http import HttpRequest

def home(request):
    id = request.COOKIES.get("user", None)
    search = request.GET.get("search", "")
    Posts = Post.objects.filter(is_draft=False).filter(title__icontains=search).all()

    return render(request, "home.html", {"id": id, "Posts": Posts})


def signin(request):
    if request.method == "POST":
        form = UserSigninForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.filter(
                username=cd["username"], password=cd["password"]
            ).first()

            if user is not None:
                response = HttpResponseRedirect("/")
                response.set_cookie("user", user.id)
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


def profile(request):
    id = request.COOKIES.get("user", None)
    if id != None:
        user = User.objects.filter(id=id).first()
        return render(request, "profile.html", {"user": user})
    else:
        return redirect("signin")


def edit(request, user_id):
    id = request.COOKIES.get("user", None)
    if id != None:
        update = User.objects.get(id=user_id)
        if request.method == "POST":
            form = UserEditForm(request.POST, request.FILES, instance=update)
            if form.is_valid():

                form.save()
                return redirect("profile")

        else:
            form = UserEditForm(instance=update)

        return render(request, "edit.html", {"form": form})
    else:
        return redirect("signin")
