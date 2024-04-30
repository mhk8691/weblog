from django.urls import path
from . import views

urlpatterns = [
    # path("user/", views.list_user, name="AllUser"),
    path("user/<int:user_id>", views.get_user_by_id, name="GetUser"),
    path("user", views.add_user, name="CreateUser"),
    path("user/<int:user_id>/", views.update_user_by_id, name="UpdateUser"),
    # path("user/<int:user_id>", views.delete_user, name="DeleteUser"),
]
