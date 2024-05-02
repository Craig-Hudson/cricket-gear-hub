from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, F
from .models import Product, Category, Size, Review
from .forms import ProductForm, ReviewForm, EditReviewForm
import uuid


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

        # Sorting by price, rating, or category
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'price':
                products = products.order_by('price')
            elif sort == 'rating':
                products = products.annotate(avg_rating=Avg('rating')).order_by('-avg_rating')
            elif sort == 'category':
                products = products.order_by('category__name')

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


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('individual_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('individual_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home')) 
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def add_review(request, product_id):
    """Add reviews to an individual product"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            if request.user.is_authenticated:
                review.user = request.user
            else:
                review.user = None
                review.identifier = str(uuid.uuid4())
            
            review.product = product
            review.save()
            messages.success(request, 'Successfully Added Review ')
            return redirect(reverse('individual_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to add Review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'products/individual_products.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Edit a review """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    # Check if the logged-in user is the owner of the review
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Review updated successfully.')
                return redirect(reverse('individual_product', args=[product.id]))
            else:
                messages.error(request, 'Failed to update review. Please check the form.')
        else:
            form = ReviewForm(instance=review)
        return render(request, 'products/individual_products.html', {'form': form})
    elif review.user is None and review.identifier == request.POST.get('identifier'):
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Review updated successfully.')
                return redirect(reverse('individual_product', args=[product.id]))
            else:
                messages.error(request, 'Failed to update review. Please check the form.')
        else:
            form = ReviewForm(instance=review)
        return render(request, 'products/individual_products.html', {'form': form})
    else:
        messages.error(request, 'You are not authorized to edit this review.')
        return redirect(reverse('individual_product', args=[product.id]))




# @login_required
# def delete_review:

