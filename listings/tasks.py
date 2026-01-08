
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(user_email, booking_id):
    send_mail(
        "Booking Confirmation",
        f"Your booking (ID: {booking_id}) has been successfully created.",
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
    )
