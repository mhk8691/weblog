from django.urls import path
from . import views

urlpatterns = [
    path("comment", views.manage_comment, name="manage_comment"),
    path("comment/<int:comment_id>", views.crud, name="crud"),
]
