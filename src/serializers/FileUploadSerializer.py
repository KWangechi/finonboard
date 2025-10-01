from rest_framework import serializers
from src.models import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"
        read_only_fields = ["id", "uploaded_at"]
