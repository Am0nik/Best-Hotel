from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_name', 'guest_email', 'guest_phone', 'room_type', 'check_in', 'check_out', 'guests_count', 'special_requests']
        
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'guest_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'guest_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'guest_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (7XX) XXX-XX-XX'}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),
            'guests_count': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Special requests...'}),
        }
