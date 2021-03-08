from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'There is nothing in the cart')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IShbAIAINsZzzXrnsBkGuEF9jn8KSonTm6WiYD7bboKPK2Noz4vK73eoNTAjw3oaGMxvejU35G7UmiJtbTI9J0000pu7eARzb',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
