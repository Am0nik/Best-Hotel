from django.db import models
from django.utils import timezone

class Booking(models.Model):
    #room types
    ROOM_CHOICES = [
        ('SINGLE', 'Single Room'),
        ('DOUBLE', 'Double Room'),
        ('SUITE', 'Deluxe Suite'),
    ]

    #rent status
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    guest_name = models.CharField(max_length=150, verbose_name="Guest's name")
    guest_email = models.EmailField(verbose_name="Email")
    guest_phone = models.CharField(max_length=20, verbose_name="Phone number")
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES, verbose_name="Room type")
    check_in = models.DateField(verbose_name="Check-in date")
    check_out = models.DateField(verbose_name="Departure date")
    guests_count = models.PositiveIntegerField(default=1, verbose_name="Number of guests")
    special_requests = models.TextField(blank=True, null=True, verbose_name="Special requests")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', verbose_name="Status")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Request creation date")

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Booking"
        ordering = ['-created_at']

    def __str__(self):
        return f"Бронь от {self.guest_name} ({self.get_room_type_display()})"
