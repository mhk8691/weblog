from django.shortcuts import render,redirect
from .forms import CreatePost
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
                return redirect('profile')
        else:
            form = CreatePost()

        return render(request, "CreatePost.html", {"form": form,'id':id})
    else:
        return redirect("signin")
