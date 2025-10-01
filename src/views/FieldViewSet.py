from rest_framework import viewsets
from rest_framework import filters
from src.models import FormField
from src.serializers.FieldSerializer import FieldSerializer

class FieldViewSet(viewsets.ModelViewSet):
    queryset = FormField.objects.all()
    serializer_class = FieldSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']