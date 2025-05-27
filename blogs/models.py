"""Blog models."""

from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel
from django.utils.text import slugify
from django.urls import reverse
from accounts.models import UserModel


class Blog(TimeStampedModel):
    """Blog page model."""

    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blog_author",
    )
    image = models.ImageField(upload_to="blog_images", null=True)
    content = models.TextField(null=True)
    category = models.CharField(max_length=255, null=True)
    tags = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    featured_by = models.CharField(max_length=255, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author} on {self.published_date}"

    def create_slug(self):
        """Create a slug for the blog post."""
        if not self.slug:
            self.slug = slugify(self.title)
            self.save()
        return self.slug

    def get_absolute_url(self):
        return reverse("blogs:detail", args=[str(self.slug)])
