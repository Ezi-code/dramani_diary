from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from core.models import NewsLetterSubscription
from core.anagers import (
    send_subscription_success_email,
    send_subscription_failure_email,
)


@receiver(post_save, sender=NewsLetterSubscription)
def subscribe_user(sender, instance, created, **kwargs):
    """
    Signal to handle user subscription.
    """
    if created:
        try:
            send_subscription_success_email(instance.email)
        except Exception as e:
            send_subscription_failure_email(instance.email)
