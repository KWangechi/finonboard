from rest_framework import serializers
from src.models import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = [
            "id",
            "submission",
            "field",
            "file",
            "uploaded_at",
        ]
        read_only_fields = ["id", "uploaded_at"]
