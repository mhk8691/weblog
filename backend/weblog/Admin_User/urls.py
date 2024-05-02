from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.list_user, name="AllUser"),
    path("user", views.add_user, name="CreateUser"),
    path("user/<int:user_id>", views.crud, name="DeleteUser"),
]
