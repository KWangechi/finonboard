from rest_framework import serializers
from src.models import Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
