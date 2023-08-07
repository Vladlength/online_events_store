from event_information.models import Event
from django.shortcuts import render
from cart.forms import CartAddProductForm


def prices(request, pk):
    event = Event.objects.get(pk=pk)
    prices = Event.objects.get(pk=pk).prices.all().order_by('price')
    cart_product_form = CartAddProductForm()
    context = {'event': event,
               'prices': prices,
               'cart_product_form': cart_product_form,
               }
    return render(request, 'ticket_prices.html', context)
