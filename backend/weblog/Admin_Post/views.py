from django.http import JsonResponse
from django.shortcuts import render
from Blog.models import Post
from .serializers import PostSerializer
import json

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from User.models import User
from Categories.models import Category


@api_view(["GET"])
def list_post(request):
    if request.method == "GET":
        Post = Post.objects.all()
        serialize = PostSerializer(Post, many=True)
        response = serialize.data
        response.headers["Access-Control-Expose-Headers"] = "Content-Range"
        response.headers["Content-Range"] = len(Post)
        return Response(response)


def get_post(post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post)
    return serializer.data


@api_view(["POST"])
def add_post(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        author = json_data.get("author")
        title = json_data.get("title")
        content = json_data.get("content")
        is_draft = json_data.get("is_draft")
        categories = json_data.get("categories")
        user = User.objects.get(id=author)
        category = Category.objects.get(id=categories)
        post = Post.objects.create(
            author=user,
            title=title,
            content=content,
            is_draft=is_draft,
            categories=category,
        )
        serializer = PostSerializer(get_post(post_id=post.id))
        return Response(serializer.data)


@api_view(["DELETE", "GET", "PUT"])
def crud(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "GET":
        post = get_post(post_id=post_id)

        return Response(post)
    elif request.method == "DELETE":
        try:
            post.delete()
            return Response({"id": post_id})
        except Post.DoesNotExist:
            return JsonResponse({"error": "User not found"})
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(get_post(post_id))
        else:
            return Response(serializer.errors)
            # response = JsonResponse(get_user(user_id), safe=False)
