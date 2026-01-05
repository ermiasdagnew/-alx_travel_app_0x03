from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime

@shared_task
def send_booking_confirmation_email(customer_email, booking_id):
    subject = f"Booking Confirmation #{booking_id}"
    message = f"Dear Customer,\n\nYour booking (ID: {booking_id}) has been successfully confirmed."
    from_email = "noreply@alxtravel.com"
    recipient_list = [customer_email]

    send_mail(subject, message, from_email, recipient_list)

    # Log sent email
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("/tmp/booking_email_log.txt", "a") as f:
        f.write(f"{timestamp} Sent booking confirmation to {customer_email} for booking {booking_id}\n")
