from rest_framework import serializers
from src.models import FormField


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
