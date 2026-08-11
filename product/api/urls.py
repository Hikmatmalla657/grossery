from django.urls import path

from .view import ProductDetailAPIView, ProductListAPIView

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="product-create"),
    path(
        "products/edit-delete-get-product/<int:pk>/",
        ProductDetailAPIView.as_view(),
        name="product-detail",
    ),
]
