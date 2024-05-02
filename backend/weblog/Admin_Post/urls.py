from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.list_post, name="AllPost"),
    path("post", views.add_post, name="PostCreate"),
    path("post/<int:post_id>", views.crud, name="crud"),
]
