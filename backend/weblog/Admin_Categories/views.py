import json
from django.http import JsonResponse
from django.shortcuts import render

from Categories.models import Category
from .serializers import CategorySerializer

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def list_category(request):
    if request.method == "GET":
        category = Category.objects.all()
        serialize = CategorySerializer(category, many=True)
        response = serialize.data
        response.headers["Access-Control-Expose-Headers"] = "Content-Range"
        response.headers["Content-Range"] = len(category)
        return Response(response)


def get_category(category_id):
    category = Category.objects.get(id=category_id)
    serializer = CategorySerializer(category)
    return serializer.data


@api_view(["POST"])
def add_category(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        name = json_data.get("name")

        category = Category.objects.create(name=name)
        serializer = CategorySerializer(get_category(category_id=category.id))
        return Response(serializer.data)


@api_view(["DELETE", "GET", "PUT"])
def crud(request, category_id):
    category = Category.objects.get(pk=category_id)

    if request.method == "GET":

        return Response(get_category(category_id))
    elif request.method == "DELETE":
        try:
            category.delete()
            return Response({"id": category_id})
        except Category.DoesNotExist:
            return JsonResponse({"error": "User not found"})
    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(get_category(category_id))
        else:
            return Response(serializer.errors)
