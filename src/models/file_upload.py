from django.db import models
from django.forms import ValidationError
from .submission import Submission
from .field import FormField
from os import path as os_path


class FileUpload(models.Model):
    submission = models.ForeignKey(
        Submission, related_name="files", on_delete=models.CASCADE
    )
    field = models.ForeignKey(FormField, on_delete=models.SET_NULL, null=True, blank=True)

    def upload_to(instance, filename):
        form_name = (
            instance.submission.form.name.lower().replace(" ", "_")
            if hasattr(instance.submission, "form")
            else "unknown_form"
        )
        return f"{form_name}/uploads/{filename}"

    file = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File for Submission {self.submission.id} - Field: {self.field.label if self.field else 'N/A'}"

    def clean(self):
        ext = os_path.splitext(self.file.name)[1].lower().replace(".", "")
        allowed_types = self.submission.form.accepted_file_types
        if allowed_types and ext not in allowed_types:
            raise ValidationError(
                f"File type {ext} not allowed. Allowed: {allowed_types}"
            )
