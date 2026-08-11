from django.urls import path

from .view import UserDetailAPIView, UserListAPIView

urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="user-create"),
    path(
        "users/edit-delete-get-user/<int:pk>/",
        UserDetailAPIView.as_view(),
        name="user-detail",
    ),
]
