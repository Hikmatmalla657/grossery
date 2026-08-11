from rest_framework import serializers

from suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name", "email", "phone", "address", "created_at", "updated_at", "is_active"]
        read_only_fields = ["id", "created_at", "updated_at"]
