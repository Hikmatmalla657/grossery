from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "password",
            "created_at",
            "updated_at",
            "address",
            "role",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
