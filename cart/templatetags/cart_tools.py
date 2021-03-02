from django import template
from django.shortcuts import get_object_or_404
from products.models import Product

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

