from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from .models import Booking

def book_a_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            messages.success(
                request,
                f"Thank you, {booking.guest_name}! Your booking request has been received. "
                f"We will contact you shortly at {booking.guest_email} to confirm your stay."
            )
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'booking_room.html', {'form': form})


def booking_success(request):
    return render(request, 'booking_success.html')

@login_required(login_url='admin_login')
def admin_page(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        new_status = request.POST.get('status')
        
        try:
            booking = Booking.objects.get(id=booking_id)
        except (Booking.DoesNotExist, ValueError):
            raise SuspiciousOperation("Invalid booking ID.")

        if new_status in dict(Booking.STATUS_CHOICES):
            booking.status = new_status
            booking.save()
            messages.success(request, f"Booking #{booking.id} status changed to {booking.get_status_display()}.")
        else:
            raise SuspiciousOperation("Invalid status value.")
        
        return redirect('admin_page')

    bookings = Booking.objects.all()
    return render(request, 'admin.html', {'bookings': bookings})

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_page')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'admin_login.html', {'form': form})

@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')