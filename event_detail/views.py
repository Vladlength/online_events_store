from django.shortcuts import render, get_object_or_404
from event_information.models import Event
from cart.forms import CartAddProductForm


def detail(request, pk):
    event = Event.objects.get(pk=pk)

    context = {
        'event': event,
    }
    return render(request, 'event_detail.html', context)



