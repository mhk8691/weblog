from django.urls import path
from . import views

urlpatterns = [
    path("user", views.manage_user, name="manage_user"),
    path("user/<int:user_id>", views.crud, name="DeleteUser"),
]
