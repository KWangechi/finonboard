from django.db import models
from .form import Form


class Field(models.Model):
    FIELD_TYPES = [
        ("text", "Text"),
        ("number", "Number"),
        ("date", "Date"),
        ("dropdown", "Dropdown"),
        ("checkbox", "Checkbox"),
        ("file", "File Upload"),
    ]

    form = models.ForeignKey(Form, related_name="fields", on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=FIELD_TYPES)
    required = models.BooleanField(default=False)
    options = models.JSONField(blank=True, null=True)
    validation_rules = models.JSONField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.label} ({self.type})"

    @property
    def parsed_options(self):
        """Ensure options always return a list, even if null/empty."""
        return self.options or []
