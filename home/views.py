from django.shortcuts import render

from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page and display the 
    4 newest products as featured products on the home page
    """
    featured_products = Product.objects.order_by('-id')[:4]

    context = {
        'featured_products' : featured_products
    }
    return render(request, 'home/index.html', context)
