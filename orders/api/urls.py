from django.urls import path
from .view import OrderDetailAPIView, OrderListAPIView

urlpatterns = [
    path("create/", OrderListAPIView.as_view(), name="order-create"),
    path(
        "edit-delete-get-order/<int:pk>/",
        OrderDetailAPIView.as_view(),
        name="order-detail",
    ),
]
