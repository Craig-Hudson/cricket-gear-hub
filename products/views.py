from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg
from .models import Product, Category


def all_products(request):
    """ A view to return the products page including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You didn\'t enter any search criteria')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        # sorting by price lowest to highest and sorting by rating highest to lowest
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'price':
                products = products.order_by('price')
            elif sort == 'rating':
                products = products.annotate(avg_rating=Avg('rating')).order_by('-avg_rating')

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'sort': sort
    }

    return render(request, 'products/products.html', context)



def individual_product(request, product_id):
    """ A view to return indivual products on their own page"""

    product = get_object_or_404(Product, pk=product_id)

    # Ensures sizes are displayed smallest to largest
    sizes = product.sizes.all().order_by('name')

    context = {
        'product': product,
    }

    return render(request, 'products/individual_products.html', context)

