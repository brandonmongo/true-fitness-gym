from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def true_products(request):
    """ A view to display all the products """
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/true_products.html', context)


def true_product_details(request, product_id):
    """ A view to display the product detail """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/true_products_details.html', context)
