from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class NewsLetterSubscription(TimeStampedModel):
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email
