from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def true_products(request):
    """ A view to display all the products """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'true-search' in request.GET:
            query = request.GET['true-search']
            if not query:
                messages.error(request, 'You didnt search anything')
                return redirect(reverse('products'))

            queries = (
                        Q(Name__icontains=query) | Q(product_description__icontains=query) | Q(Brand__icontains=query))
            products = products.filter(queries)

    context = {
        'products': products,
        'search_product': query
    }

    return render(request, 'products/true_products.html', context)


def true_product_details(request, product_id):
    """ A view to display the product detail """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/true_products_details.html', context)
