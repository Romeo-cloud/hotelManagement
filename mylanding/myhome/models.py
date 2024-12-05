from django.db import models

# Create your models here.

# class Booking(models.Model):
#     room_choices = [
#         ('executive', 'Executive'),
#         ('standard', 'Standard'),
#     ]
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     checkin_date = models.DateField()
#     checkout_date = models.DateField()
#     adult_count = models.PositiveIntegerField()
#     children_count = models.PositiveIntegerField()
#     room_type = models.CharField(max_length=20, choices= room_choices )
#     rooms = models.PositiveIntegerField()


#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.name} - {self.room_type} ({self.checkin_date} to {self.checkout_date})'



from django.db.models import Q

class Booking(models.Model):
    ROOM_CHOICES = [
        ('standard', 'Standard'),
        ('executive', 'Executive'),
    ]

    ROOM_RANGES = {
        'standard': range(1, 9),  # Rooms 1-8
        'executive': range(9, 13),  # Rooms 9-12
    }

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    adult_count = models.PositiveIntegerField()
    children_count = models.PositiveIntegerField()
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES)
    rooms = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - Room {self.rooms} ({self.checkin_date} to {self.checkout_date})'

    @staticmethod
    def available_rooms(room_type, checkin_date, checkout_date):
        """
        Finds available rooms for the given type and date range.
        """
        all_rooms = list(Booking.ROOM_RANGES[room_type])
        booked_rooms = Booking.objects.filter(
            Q(room_type=room_type) &
            Q(checkin_date__lt=checkout_date) &
            Q(checkout_date__gt=checkin_date)
        ).values_list('rooms', flat=True)
        return [room for room in all_rooms if room not in booked_rooms]
    
#  model for contact us
class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted At")

    def __str__(self):
        return f"Message from {self.name} ({self.email}) on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

