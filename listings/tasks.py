from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime

@shared_task
def send_booking_confirmation_email(customer_email, booking_id):
    subject = f"Booking Confirmation #{booking_id}"
    message = f"Dear Customer, your booking (ID: {booking_id}) has been confirmed."
    send_mail(subject, message, "noreply@alxtravel.com", [customer_email])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("/tmp/booking_email_log.txt", "a") as f:
        f.write(f"{timestamp} Sent booking email to {customer_email}\n")
