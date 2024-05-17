import json
from django.shortcuts import render
from flask_cors import cross_origin
from User.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse


@api_view(["GET"])
def list_user(request):
    # if request.method == "GET":
    #     Users = User.objects.all()
    #     serialize = UserSerializer(Users, many=True)
    #     range = request.GET.get("range")
    #     sort = request.GET.get("sort")
    #     print(range)
    #     print(sort)
    #     response = serialize.data
    #     response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    #     response.headers["Content-Range"] = len(Users)

    #     return Response(response)
    range = request.GET["range"]
    sort = request.GET["sort"]
    final_range = json.loads(range)
    final_sort = json.loads(sort)
    if final_sort[1] == "DESC":
        users = User.objects.all().order_by("-{}".format(final_sort[0]))[
            final_range[0] : final_range[1]
        ]
    else:
        users = User.objects.all().order_by(final_sort[0])[
            final_range[0] : final_range[1]
        ]
    serializer = UserSerializer(users, many=True)
    response = Response(serializer.data)
    response["Content-Range"] = f"users 0-{len(users)-1}/{len(users)}"
    response["Access-Control-Expose-Headers"] = "Content-Range"
    return response


def get_user(user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return serializer.data


@api_view(["POST"])
def add_user(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        username = json_data.get("username")
        password = json_data.get("password")
        email = json_data.get("email")
        user = User.objects.create(username=username, email=email, password=password)
        # serializer = UserSerializer()
        return Response(get_user(user_id=user.id))


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
