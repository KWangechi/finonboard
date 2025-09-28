# models/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .submission import Submission

# from forms.tasks import notify_admin


@receiver(post_save, sender=Submission)
def submission_created(sender, instance, created, **kwargs):
    if created:
        print(f"New submission created with ID: {instance.id}")
        # notify_admin.delay(instance.id)
