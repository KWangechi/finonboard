from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from src.models.field import FormField


class Form(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField(blank=True, null=True)
    allow_multiple_uploads = models.BooleanField(default=False)
    accepted_file_types = models.JSONField(default=list)

    created_by = models.ForeignKey(
        User, related_name="forms_created", on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User,
        related_name="forms_updated",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    
    form_fields = models.ManyToManyField(FormField, related_name='forms')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
