from cart.cart import Cart


# it is designed to transfer the cart object to the template context when rendering the page.
def cart(request):
    return {'cart': Cart(request)}
