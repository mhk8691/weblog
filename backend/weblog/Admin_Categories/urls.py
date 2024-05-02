from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.list_category, name="AllCategory"),
    path("category", views.add_category, name="CategoryCreate"),
    path("category/<int:category_id>", views.crud, name="crud"),
]
