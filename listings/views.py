
from rest_framework import viewsets
from .tasks import send_booking_confirmation_email

class BookingViewSet(viewsets.ViewSet):
    def perform_create(self, serializer):
        booking = serializer.save()
        send_booking_confirmation_email.delay("test@example.com", booking.id)
