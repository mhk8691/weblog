from django.urls import path
from . import views

urlpatterns = [
    path("category", views.manage_category, name="manage_category"),
    path("category/<int:category_id>", views.crud, name="crud"),
]
