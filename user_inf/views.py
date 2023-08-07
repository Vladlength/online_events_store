from django.shortcuts import render
from cart.models import Purchase, Booking
from django.conf import settings


def user_inf(request):
    events = Purchase.objects.all().filter(user=request.user).order_by('-created_on')
    booked_events = Booking.objects.all().filter(user=request.user).order_by('-created_on')
    key = settings.STRIPE_PUBLISHABLE_KEY

    context = {
        'events': events,
        'booked_events': booked_events,
        'key': key
    }
    return render(request, r'user_inf\user_page.html', context)
