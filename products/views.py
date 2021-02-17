from django.shortcuts import render
from .models import Product

# Create your views here.


def true_products(request):
    """ A view to display all the products """
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/true_products.html', context)
