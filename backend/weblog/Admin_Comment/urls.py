from django.urls import path
from . import views

urlpatterns = [
    path("comment/", views.list_comment, name="AllComment"),
    path("comment", views.add_comment, name="CommentCreate"),
    path("comment/<int:comment_id>", views.crud, name="crud"),
]
