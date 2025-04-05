"""
Managers for the core app."""

from django.core.mail import send_mail, EmailMessage


def send_subscription_success_email(email):
    """
    Send a subscription success email to the user.
    """
    # Logic to send email
    subject = "Subscription Successful"
    message = "Thank you for subscribing to our newsletter!"
    from_email = "noreply@dramani_diary.com"
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    # You can customize the email content as needed


def send_subscription_failure_email(email):
    """
    Send a subscription failure email to the user.
    """
    # Logic to send email
    subject = "Subscription Failed"
    message = "There was an issue with your subscription. Please try again."
    from_email = "noreply@dramani_diary.com"
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    # You can customize the email content as needed


def send_unsubscription_email(email):
    """
    Send an unsubscription email to the user.
    """
    # Logic to send email
    subject = "Unsubscription Successful"
    message = "You have successfully unsubscribed from our newsletter."
    from_email = "noreply@dramani_diary.com"
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    # You can customize the email content as needed


def send_unsubscription_failure_email(email):
    """
    Send an unsubscription failure email to the user.
    """
    # Logic to send email
    subject = "Unsubscription Failed"
    message = "There was an issue with your unsubscription. Please try again."
    from_email = "noreply@dramani_diary.com"
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    # You can customize the email content as needed
