from django.shortcuts import render, redirect
from .forms import CreatePost,UpdatePost
from User.models import User
from .models import Post
from django.contrib import messages


def Create(request):
    id = request.COOKIES.get("user", None)
    if id != None:
        if request.method == "POST":
            form = CreatePost(request.POST, request.FILES)
            users = User.objects.get(id=id)
            if form.is_valid():
                cd = form.cleaned_data
                Post.objects.create(
                    author=users,
                    title=cd["title"],
                    content=cd["content"],
                    image=cd["image"],
                )
                messages.success(request, "success", "success")
                return redirect("profile")
        else:
            form = CreatePost()

        return render(request, "CreatePost.html", {"form": form, "id": id})
    else:
        return redirect("signin")


def ShowPost(request):
    id = request.COOKIES.get("user", None)
    if id != None:
        user = User.objects.get(id=id)
        Posts = Post.objects.all().filter(author=user)

        object_posts = {"Posts": Posts}

        return render(request, "profile.html", object_posts)
    else:
        return redirect("signin")


def publish(request, post_id):
    id = request.COOKIES.get("user", None)
    if id != None:
        Post.objects.filter(id=post_id).update(is_draft=False)
        return redirect("profile")
    else :
        return redirect("signin")

def detail(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, "detail.html",{'post':post})

def delete_post(request,post_id):
    id = request.COOKIES.get("user", None)
    if id != None:
        Post.objects.get(id=post_id).delete()
        return redirect('profile')
    else:
        return redirect('signin')

def update_post(request,post_id):
    update = Post.objects.get(id=post_id)
    
    if request.method == 'POST':
        form = UpdatePost(request.POST, request.FILES,instance=update)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UpdatePost(instance=update)
        return render(request,'UpdatePost.html',{'form':form})