from django import template

# filters for templates

register = template.Library()


@register.filter
def prices_sort(prices):
    return prices.order_by('price')


@register.filter
def quantity_is_zero(quantity):
    if quantity == 0:
        return True


@register.filter
def mul_100(price):
    price *= 100
    return price


@register.filter
def int_(price):
    return int(price)
