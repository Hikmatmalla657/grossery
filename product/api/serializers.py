from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "expiry_date",
            "price",
            "quantity",
            "category",
        ]
        read_only_fields = ["id", "created_at"]
