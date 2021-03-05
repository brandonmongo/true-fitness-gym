from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_cart(request):
    """ A view that returns the shopping cart content """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ A view that adds product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    selected_flavor = None

    selected_flavor = request.POST.get('flavor')

    cart = request.session.get('cart', {})

    if selected_flavor:
        if product_id in list(cart.keys()):
            if selected_flavor in cart[product_id]['product_by_flavor'].keys():
                cart[product_id]['product_by_flavor'][selected_flavor] += quantity
            else:
                cart[product_id]['product_by_flavor'][selected_flavor] = quantity
        else:
            cart[product_id] = {'product_by_flavor': {selected_flavor: quantity}}
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

    selected_flavor = None
    selected_flavor = request.POST.get('selected_flavor')

    cart = request.session.get('cart', {})

    if selected_flavor:
        if quantity > 0:
            cart[product_id]['product_by_flavor'][selected_flavor] = quantity
        else:
            del cart[product_id]['product_by_flavor'][selected_flavor]
            if not cart[product_id]['product_by_flavor']:
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
        selected_flavor = None
        selected_flavor = request.POST['selected_flavor']
        print(selected_flavor)
        cart = request.session.get('cart', {})

        if selected_flavor:
            del cart[product_id]['product_by_flavor'][selected_flavor]
            print(cart)
            if not cart[product_id]['product_by_flavor']:
                cart.pop(product_id)
        else:
            cart.pop(product_id)

        request.session['cart'] = cart
        print(request.session['cart'])
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
