from django.urls import path
from . import views

urlpatterns = [
    path("Create/", views.Create, name="create"),
    path("profile/show/", views.ShowPost, name="show"),
    path("publish/<int:post_id>", views.publish, name="publish"),
    # path("create/", views.create, name="create"),
    # path("detail/<int:blog_id>", views.detail, name="detail"),
    # path("update/<int:blog_id>", views.update, name="update"),
    # path("delete/<int:blog_id>", views.delete, name="delete"),
]
