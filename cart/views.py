from event_information.models import Event
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cart.cart import Cart
from .forms import CartAddProductForm
from django.conf import settings
import stripe
from django.contrib.auth.decorators import login_required
from .models import Purchase, Booking

stripe.api_key = settings.STRIPE_SECRET_KEY  # key for pay


@require_POST  # so that it can only be accessed with the POST method
def cart_add(request, product_id, price_id):
    Cart.__init__(Cart, request=request, clear=True)
    cart = Cart(request)
    product = Event.objects.get(id=product_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 price_id=price_id,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Event, id=product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')


# to view entries
def cart_detail(request):
    cart = Cart(request)
    key = settings.STRIPE_PUBLISHABLE_KEY
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})

    return render(request, 'cart/detail.html', {'cart': cart, 'key': key})


def cart_clear(request):
    Cart.__init__(Cart, request=request, clear=True)
    return redirect('index')


# only for login users
# make a purchase
@login_required
def cart_charge(request, event_id, quantity, price, price_id, flag=1):  # for pay
    event = Event.objects.get(id=event_id)

    event_name = event.name
    price = price
    image = event.image
    quantity = quantity

    purchase = Purchase(user=request.user, event_name=event_name, price=price, image=image, quantity=quantity)
    purchase.save()
    if flag:
        price = event.prices.get(id=price_id)
        price.tickets_quantity -= quantity
        price.save()
    # if pay from booking
    else:
        purchase = Booking.objects.get(event_id=event_id, price_id=price_id, quantity=quantity)
        purchase.delete()

    return render(request, 'cart/charge.html', )


# only for login users
# make a booking
@login_required
def booking_cart(request, event_id, quantity, price, price_id):  # for booking
    event = Event.objects.get(id=event_id)

    event_name = event.name
    price = price
    image = event.image
    quantity = quantity

    booking = Booking(user=request.user, event_name=event_name, price=price, image=image, quantity=quantity,
                      event_id=event_id, price_id=price_id)
    booking.save()

    price = event.prices.get(id=price_id)
    price.tickets_quantity -= quantity
    price.save()
    return redirect('user_page')
