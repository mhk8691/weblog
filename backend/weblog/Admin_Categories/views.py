from django.shortcuts import render

from Categories.models import Category
from .serializers import CategorySerializer

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_all_category():
    Categories = Category.objects.all()
    serialize = CategorySerializer(Categories, many=True)
    return serialize.data


@api_view()
def list_category(request):
    response_data = get_all_category()

    return Response(response_data)


def get_category(category_id):
    category = Category.objects.get(id=category_id)
    serializer = CategorySerializer(category)
    return serializer.data


@api_view()
def get_category_by_id(request, category_id):
    category = get_category(category_id)
    if category is None:
        return "", 404
    # response = JsonResponse(user, safe=False)
    return Response(category)
