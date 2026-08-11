from django.urls import path

from .view import SupplierDetailAPIView, SupplierListAPIView

urlpatterns = [
    path("suppliers/", SupplierListAPIView.as_view(), name="supplier-create"),
    path(
        "suppliers/edit-delete-get-supplier/<int:pk>/",
        SupplierDetailAPIView.as_view(),
        name="supplier-detail",
    ),
]
