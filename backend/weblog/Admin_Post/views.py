from django.shortcuts import render
from Blog.models import Post
from .serializers import PostSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

def get_all_post():
    Posts = Post.objects.all()
    serialize = PostSerializer(Posts, many=True)
    return serialize.data


@api_view()
def list_post(request):
    response_data = get_all_post()

    return Response(response_data)


def get_post(post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post)
    return serializer.data


@api_view()
def get_post_by_id(request, post_id):
    post = get_post(post_id)
    if post is None:
        return "", 404
    # response = JsonResponse(user, safe=False)
    return Response(post)
