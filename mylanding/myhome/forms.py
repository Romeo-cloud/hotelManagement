# from django import forms
# from .models import Booking

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['name', 'email', 'phone_number', 'checkin_date', 'checkout_date', 'adult_count', 'children_count', 'room_type', 'rooms']
#         widgets = {
#             'checkin_date': forms.DateInput(attrs={'type': 'date'}),
#             'checkout_date': forms.DateInput(attrs={'type': 'date'}),
#         }

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'phone_number', 'checkin_date', 'checkout_date',
            'adult_count', 'children_count', 'room_type', 'rooms'
        ]
        widgets = {
            'checkin_date': forms.DateInput(attrs={'type': 'date'}),
            'checkout_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        room_type = cleaned_data.get('room_type')
        checkin_date = cleaned_data.get('checkin_date')
        checkout_date = cleaned_data.get('checkout_date')
        rooms = cleaned_data.get('rooms')

        if room_type and checkin_date and checkout_date:
            # Check if the room is available
            available_rooms = Booking.available_rooms(room_type, checkin_date, checkout_date)
            if rooms not in available_rooms:
                raise forms.ValidationError(
                    f"Room {rooms} is not available for the selected dates. "
                    f"Available rooms: {', '.join(map(str, available_rooms))}."
                )
        return cleaned_data
