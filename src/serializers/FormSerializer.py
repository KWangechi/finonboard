from rest_framework import serializers
from src.models import Form


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "allow_multiple_uploads",
            "accepted_file_types",
            "created_by",
            "updated_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]
