from django.urls import path
from . import views

urlpatterns = [
    path("Create/", views.Create, name="create"),
    path("profile/show/", views.ShowPost, name="show"),
    path("publish/<int:post_id>", views.publish, name="publish"),
    # path("create/", views.create, name="create"),
    path("detail/<int:post_id>", views.detail, name="detail"),
    path("update/<int:post_id>", views.update_post, name="update"),
    path("delete/<int:post_id>", views.delete_post, name="delete"),
    path(
        "delete_comment/<int:post_id>/<int:comment_id>/",
        views.delete_comment,
        name="delete_comment",
    ),
    path(
        "update_comment/<int:post_id>/<int:comment_id>/",
        views.update_comment,
        name="update_comment",
    ),
]
