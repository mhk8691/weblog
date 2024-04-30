from django.urls import path
from . import views

urlpatterns = [
    path("post", views.list_post),
    path("post/<int:post_id>", views.get_post_by_id),
]
