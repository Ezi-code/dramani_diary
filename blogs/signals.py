from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Blog


@receiver(post_save, sender=Blog)
def create_slug(sender, instance, created, **kwargs):
    """Create a slug for the blog post after saving."""
    if created and not instance.slug:
        instance.slug = instance.create_slug()
        instance.save()
