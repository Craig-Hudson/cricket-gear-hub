from django.shortcuts import render

from products.models import Product

# Create your views here.

def index(request):
    """ A view to return the index page """
    featured_products = Product.objects.order_by('-id')[:4]

    context = {
        'featured_products' : featured_products
    }
    return render(request, 'home/index.html', context)


# def featured_products(request):
#     ''' Function to get the last 4 products added to be displayed as featured products'''
    
#     featured_products = Product.objects.order_by('-id')[:4]
#     print('featured_products')

#     template = 'home/index.html'
#     context = {
#         'featured_products' : featured_products,
#     }

#     return render(request, template, context)