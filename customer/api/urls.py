from django.urls import path

from .view import CustomerDetailAPIView, CustomerListAPIView

urlpatterns = [
    path("customers/", CustomerListAPIView.as_view(), name="customer-create"),
    path(
        "customers/edit-delete-get-customer/<int:pk>/",
        CustomerDetailAPIView.as_view(),
        name="customer-detail",
    ),
]
