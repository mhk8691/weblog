import json
from django.http import JsonResponse
from django.shortcuts import render

from Categories.models import Category
from .serializers import CategorySerializer

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
def manage_category(request):
    if request.method == "GET":
        range = json.loads(request.GET["range"])
        sort = json.loads(request.GET["sort"])
        filter = request.GET["filter"]
        search = regex(filter)
        if search == None:
            search = ""
        if sort[1] == "DESC":
            category = (
                Category.objects.all()
                .filter(Q(name__icontains=search))
                .order_by("-{}".format(sort[0]))[range[0] : range[1]]
            )
        else:
            category = (
                Category.objects.all()
                .filter(Q(name__icontains=search))
                .order_by(sort[0])[range[0] : range[1]]
            )
        serializer = CategorySerializer(category, many=True)
        response = Response(serializer.data)
        response["Content-Range"] = f"category 0-{len(category)-1}/{len(category)}"
        response["Access-Control-Expose-Headers"] = "Content-Range"
        return response
    elif request.method == "POST":
        json_data = json.loads(request.body)
        name = json_data.get("name")

        category = Category.objects.create(name=name)
        return Response(get_category(category_id=category.id))


def get_category(category_id):
    category = Category.objects.get(id=category_id)
    serializer = CategorySerializer(category)
    return serializer.data


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
