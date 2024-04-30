import json
from django.shortcuts import render
from User.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


def get_all_user():
    Users = User.objects.all()
    serialize = UserSerializer(Users, many=True)
    return serialize.data


@api_view()
def list_user(request):
    response_data = get_all_user()

    return Response(response_data)


def get_user(user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return serializer.data


@api_view()
def get_user_by_id(request, user_id):
    user = get_user(user_id)
    if user is None:
        return "", 404
    # response = JsonResponse(user, safe=False)
    return Response(user)


def create_user(username, email, password):

    user = User.objects.create(username=username, email=email, password=password)
    user_id = user.id
    print(user_id)

    return user_id


@api_view()
def add_user(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_id = create_user(username, password, email)
        return Response(user_id), 201
    else:
        print("hello")


def update_user(user_id, username, password, email):
    User.objects.filter(id=user_id).update(
        username=username, password=password, email=email
    )
    return get_user(user_id)


def update_user_by_id(request, user_id):
    if request.method == "POST":
        username = request.JSON.get["username"]
        password = request.JSON.get["password"]
        email = request.JSON.get["email"]
        user = update_user(user_id, username, password, email)
        return Response(get_user(user_id)), 201
