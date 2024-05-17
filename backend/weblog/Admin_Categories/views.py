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
        range = request.GET["range"]
        sort = request.GET["sort"]
        final_range = json.loads(range)
        final_sort = json.loads(sort)
        if final_sort[1] == "DESC":
            category = Category.objects.all().order_by("-{}".format(final_sort[0]))[
                final_range[0] : final_range[1]
            ]
        else:
            category = Category.objects.all().order_by(final_sort[0])[
                final_range[0] : final_range[1]
            ]
        serializer = CategorySerializer(category, many=True)
        response = Response(serializer.data)
        response["Content-Range"] = f"category 0-{len(category)-1}/{len(category)}"
        response["Access-Control-Expose-Headers"] = "Content-Range"
        return response


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
        return Response(get_category(category_id=category.id))


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
