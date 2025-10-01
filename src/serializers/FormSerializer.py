from rest_framework import serializers
from src.models import Form


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"
        read_only_fields = ["id", "slug", "created_at", "updated_at"]
