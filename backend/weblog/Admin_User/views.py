from django.shortcuts import render
from User.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import JsonResponse
from django.http import request

def get_all_user():
    Users = User.objects.all()
    serialize = UserSerializer(Users, many=True)
    return serialize.data


def list_user(request):
    response_data = get_all_user()

    response = JsonResponse(response_data, safe=False)
    response["Access-Control-Expose-Headers"] = "Content-Range"

    content_length = len(response.content)
    response["Content-Range"] = f"bytes */{content_length}"

    return response


def get_user(user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return serializer.data


@api_view()
def get_user_by_id(request, user_id):
    user = get_user(user_id)
    if user is None:
        return "", 404
    response = JsonResponse(user, safe=False)
    return response


def create_user(username, email, password):

    user = User.objects.create(username=username, email=email, password=password)
    user_id = user.id
    print(user_id)

    return user_id

@api_view()
def add_user(request):
    if request.method == 'POST':
        name = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        request.POST.get("title", "")

        user_id = create_user(name, password, email)
        # response = JsonResponse(get_user_by_id(user_id), safe=False)
        return Response(get_user_by_id(user_id)), 201
