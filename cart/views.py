from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
# Create your views here.


def view_cart(request):
    """ A view that returns the shopping cart content """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ A view that adds product to the shopping cart """

    product = get_object_or_404(Product, pk=product_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    selected_flavor = None

    selected_flavor = request.POST.get('flavor')

    cart = request.session.get('cart', {})

    if selected_flavor:
        if product_id in list(cart.keys()):
            if selected_flavor in cart[product_id]['product_by_flavor'].keys():
                cart[product_id]['product_by_flavor'][selected_flavor] += quantity
                messages.success(request, f"Updated {product.Name} Flavour: {selected_flavor} quantity to {cart[product_id]['product_by_flavor'][selected_flavor]}")
            else:
                cart[product_id]['product_by_flavor'][selected_flavor] = quantity
                messages.success(request, f'Added {product.Name} (Flavour: {selected_flavor}) to your cart')
        else:
            cart[product_id] = {'product_by_flavor': {selected_flavor: quantity}}
            messages.success(request, f'Added Flavour {selected_flavor} {product.Name} to your cart')
    else:
        if product_id in list(cart.keys()):
            cart[product_id] += quantity
            messages.success(request, f'Updated {product.Name} quantity to {cart[product_id]}')
        else:
            cart[product_id] = quantity
            messages.success(request, f'Added {product.Name} to your cart')

    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """ A view that adjust the quantity of a specific product to the specified amount """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))

    selected_flavor = None
    selected_flavor = request.POST.get('selected_flavor')

    cart = request.session.get('cart', {})

    if selected_flavor:
        if quantity > 0:
            cart[product_id]['product_by_flavor'][selected_flavor] = quantity
            messages.success(request, f"Updated {product.Name} (Flavour: {selected_flavor}) quantity to {cart[product_id]['product_by_flavor'][selected_flavor]}")
        else:
            del cart[product_id]['product_by_flavor'][selected_flavor]
            if not cart[product_id]['product_by_flavor']:
                cart.pop(product_id)
            messages.success(request, f'Removed Flavour {selected_flavor} {product.Name} from your cart')
    else:
        if quantity > 0:
            cart[product_id] = quantity
            messages.success(request, f'Updated {product.Name} quantity to {cart[product_id]}')
        else:
            cart.pop(product_id)
            messages.success(request, f'Remove {product.Name} from the cart')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(reverse('cart'))


def remove_from_cart(request, product_id):
    """ A view to remove item from the cart """
    try:
        product = get_object_or_404(Product, pk=product_id)
        selected_flavor = None
        selected_flavor = request.POST['selected_flavor']
        print(selected_flavor)
        cart = request.session.get('cart', {})

        if selected_flavor:
            del cart[product_id]['product_by_flavor'][selected_flavor]
            print(cart)
            if not cart[product_id]['product_by_flavor']:
                cart.pop(product_id)
            messages.success(request, f'Removed {product.Name} (Flavour {selected_flavor})  from your cart')
        else:
            cart.pop(product_id)
            messages.success(request, f'Remove {product.Name} from the cart')

        request.session['cart'] = cart
        print(request.session['cart'])
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
