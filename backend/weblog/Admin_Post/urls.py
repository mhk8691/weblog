from django.urls import path
from . import views

urlpatterns = [
    path("post", views.manage_post, name="manage_post"),
    path("post/<int:post_id>", views.crud, name="crud"),
]
