from decimal import Decimal
from django.conf import settings
from event_information.models import Event


class Cart(object):

    def __init__(self, request, clear=False):
        """
        Initializing the card
        """
        # if it is true to clear, then the resulting object of the cart is cleared
        if clear:
            self.session = request.session
            cart = self.session.get(settings.CART_SESSION_ID)
            cart.clear()
        # otherwise we get a cart object

        else:
            self.session = request.session
            cart = self.session.get(settings.CART_SESSION_ID)

        # saving an EMPTY cart in the session
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        We sort through the products in the cart and get the products from the database.
        """
        event_ids = self.cart.keys()

        # we receive the goods and add them to the cart
        events = Event.objects.filter(id__in=event_ids)
        cart = self.cart.copy()
        for event in events:
            cart[str(event.id)]['product'] = event

        # used as a generator
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            item['100_price'] = item['price'] * item['quantity'] * 100
            item['int_100_price'] = int(item['price'] * item['quantity'])
            yield item

    # We count how many items are in the cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # Adding an item to the cart or updating its quantity.
    def add(self, product, price_id, quantity=1, update_quantity=False):  # new
        product_id = str(product.id)
        if product_id not in self.cart or product.prices.get(pk=price_id) != self.cart[product_id]['price']:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.prices.get(pk=price_id)),
                                     'price_id': price_id}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    # save the product
    def save(self):
        # The value of the cart object is stored in the session so that it can be retrieved on subsequent requests.
        self.session[settings.CART_SESSION_ID] = self.cart
        #  indicate to Django that the session has been changed and should be saved
        self.session.modified = True

    # remove product
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    # clearing the cart in the session
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
