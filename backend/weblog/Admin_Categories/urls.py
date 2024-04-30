from django.urls import path
from . import views

urlpatterns = [
    path("category", views.list_category),
    path("category/<int:category_id>", views.get_category_by_id),
]
