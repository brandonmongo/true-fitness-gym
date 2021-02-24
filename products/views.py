from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.


def true_products(request):
    """ A view to display all the products """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(Category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'true-search' in request.GET:
            query = request.GET['true-search']
            if not query:
                messages.error(request, 'You didnt search anything')
                return redirect(reverse('products'))

            queries = (
                        Q(Name__icontains=query) | Q(product_description__icontains=query) | Q(Brand__icontains=query))
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_product': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'products/true_products.html', context)


def true_product_details(request, product_id):
    """ A view to display the product detail """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/true_products_details.html', context)