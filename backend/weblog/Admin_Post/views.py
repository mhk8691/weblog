from django.http import JsonResponse
from Blog.models import Post
from .serializers import PostSerializer
import json

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from User.models import User
from Categories.models import Category
from django.db.models import Q

import re


def regex(text):
    if len(text) > 2:
        search = re.split(r""":""", text)
        search2 = re.split(r"""^{\"""", search[0])
        search2 = re.split(r"""\"$""", search2[1])
        regex_filter = re.split(rf'"{search2[0]}":"(.*?)"', text)
        return regex_filter[1]


@api_view(["GET", "POST"])
def manage_post(request):
    if request.method == "GET":
        range = request.GET["range"]
        sort = request.GET["sort"]
        filter = request.GET["filter"]
        search = regex(filter)
        if search == None:
            search = ""

        final_range = json.loads(range)
        final_sort = json.loads(sort)
        if final_sort[1] == "DESC":
            posts = Post.objects.all().filter(Q(title__icontains=search)).order_by("-{}".format(final_sort[0]))[
                final_range[0] : final_range[1]
            ]
        else:
            posts = (
                Post.objects.all()
                .filter(Q(title__icontains=search))
                .order_by(final_sort[0])[final_range[0] : final_range[1]]
            )
        serializer = PostSerializer(posts, many=True)
        response = Response(serializer.data)
        response["Content-Range"] = f"posts 0-{len(posts)-1}/{len(posts)}"
        response["Access-Control-Expose-Headers"] = "Content-Range"
        return response
    elif request.method == "POST":
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
        # serializer = PostSerializer()
        return Response(get_post(post_id=post.id))


def get_post(post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post)
    return serializer.data


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
