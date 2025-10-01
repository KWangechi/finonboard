from rest_framework import viewsets
from rest_framework import filters
from src.models import Form
from src.serializers import FormSerializer

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']