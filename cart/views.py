from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_cart(request):
    """ A view that returns the shopping cart content """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ A view that adds product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    weight = None
    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    cart = request.session.get('cart', {})

    if weight:
        if product_id in list(cart.keys()):
            if weight in cart[product_id]['product_by_weight'].keys():
                cart[product_id]['product_by_weight'][weight] += quantity
            else:
                cart[product_id]['product_by_weight'][weight] = quantity
        else:
            cart[product_id] = {'product_by_weight': {weight: quantity}}
    else:
        if product_id in list(cart.keys()):
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """ A view that adjust the quantity of a specific product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    weight = None
    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    cart = request.session.get('cart', {})

    if weight:
        if quantity > 0:
            cart[product_id]['product_by_weight'][weight] = quantity
            if not cart[product_id]['product_by_weight']:
                cart.pop(product_id)
        else:
            del cart[product_id]['product_by_weight'][weight]
            if not cart[product_id]['product_by_weight']:
                cart.pop(product_id)
    else:
        if quantity > 0:
            cart[product_id] = quantity
        else:
            cart.pop(product_id)

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(reverse('cart'))


def remove_from_cart(request, product_id):
    """ A view to remove item from the cart """
    try:
        weight = None
        if 'product_weight' in request.POST:
            weight = request.POST['product_weight']
        cart = request.session.get('cart', {})

        if weight:
            del cart[product_id]['product_by_weight'][weight]
            if not cart[product_id]['product_by_weight']:
                cart.pop(product_id)
        else:
            cart.pop(product_id)

        request.session['cart'] = cart
        print(request.session['cart'])
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
