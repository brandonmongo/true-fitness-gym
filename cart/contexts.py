from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for product_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += item_data * product.Price
            product_count += item_data
            cart_items.append({
                'product_id': product_id,
                'quantity': item_data,
                'product': product
            })
        else:
            product = get_object_or_404(Product, pk=product_id)
            for weight, quantity in item_data['product_by_weight'].items():
                total += quantity * product.Price
                product_count += quantity
                cart_items.append({
                    'product_id': product_id,
                    'quantity': item_data,
                    'product': product,
                    'weight': weight
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_delivery_gap = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_gap = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_gap': free_delivery_gap,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total
    }

    return context
