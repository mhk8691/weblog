import json
from django.shortcuts import render
from flask_cors import cross_origin
from User.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
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
def manage_user(request):
    if request.method == "GET":
        range = json.loads(request.GET["range"])
        sort = json.loads(request.GET["sort"])
        filter = request.GET["filter"]
        search = regex(filter)
        if search == None:
            search = ""
        if sort[1] == "DESC":
            users = (
                User.objects.all()
                .filter(Q(username__icontains=search))
                .order_by("-{}".format(sort[0]))[range[0] : range[1] + 1]
            )
        else:
            users = (
                User.objects.all()
                .filter(Q(username__icontains=search))
                .order_by(sort[0])[range[0] : range[1] + 1]
            )
        serializer = UserSerializer(users, many=True)
        response = Response(serializer.data)
        response["Content-Range"] = f"users 0-{len(users)-1}/{len(users)}"
        response["Access-Control-Expose-Headers"] = "Content-Range"
        return response
    elif request.method == "POST":
        json_data = json.loads(request.body)
        username = json_data.get("username")
        password = json_data.get("password")
        email = json_data.get("email")

        user = User.objects.create(username=username, email=email, password=password)
        return Response(get_user(user_id=user.id))


def get_user(user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return serializer.data


@api_view(["DELETE", "GET", "PUT"])
def crud(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "DELETE":
        if request.method == "DELETE":
            try:
                user.delete()
                return Response({"id": user_id})
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found"})
    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(get_user(user_id))
        else:
            return Response(serializer.errors)
            # response = JsonResponse(get_user(user_id), safe=False)
    elif request.method == "GET":
        user = get_user(user_id)
        return Response(user)
    else:
        return HttpResponse(404)
