from django import template
'''
filters for templates
'''

register = template.Library()


@register.filter
def smallest_price(prices):
    return prices.order_by('price').first()


@register.filter
def largest_price(prices):
    return prices.order_by('-price').first()


@register.filter
def one_price(prices):
    counter = len(prices.order_by('price').all())

    return counter == 1

@register.filter
def zero_price(prices):
    counter = len(prices.order_by('price').all())

    return counter == 0
