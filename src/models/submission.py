from django.db import models
from django.forms import ValidationError
from .form import Form
from django.contrib.auth.models import User


class Submission(models.Model):
    form = models.ForeignKey(Form, related_name="submissions", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="submissions", on_delete=models.CASCADE, null=True, blank=True)
    data = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.id} for {self.form.name}"

    def clean(self):
        """Custom validation before saving."""
        valid_field_ids = set(self.form.fields.values_list("id", flat=True))
        for field_id in self.data.keys():
            if int(field_id) not in valid_field_ids:
                raise ValidationError(f"Invalid field ID: {field_id}")

    def save(self, *args, **kwargs):
        # Run validation before saving
        self.full_clean()
        super().save(*args, **kwargs)
