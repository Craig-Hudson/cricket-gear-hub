from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.conf import settings
from products.models import Product


def view_cart(request):
    """ A view to render the cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    product = Product.objects.get(pk=item_id)

    try:
        quantity = int(request.POST.get('quantity'))
        size_id = request.POST.get('size')
        redirect_url = request.POST.get('redirect_url')
        cart = request.session.get('cart', {})

        item_key = f"{item_id}_{size_id}" if size_id else str(item_id)

        if item_key in cart:
            cart[item_key] += quantity
        else:
            cart[item_key] = quantity

        request.session['cart'] = cart
        messages.success(request, f'Added {product.name} to your bag')
        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return HttpResponse(status=500)


def update_cart(request, item_key):
    """ Update the quantity of an item in the cart """
    try:
        if request.method == 'POST':
            quantity = int(request.POST.get('quantity'))
            cart = request.session.get('cart', {})
            cart[item_key] = quantity  # Update the quantity directly
            request.session['cart'] = cart
            product_id, size_id = (
                item_key.split('_') if '_' in item_key else (item_key, None)
            )

            product = Product.objects.get(pk=product_id)
            messages.success(
                request,
                f'Quantity updated successfully for {product.name}.'
            )

        return redirect('view_cart')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('view_cart')


def remove_from_cart(request, item_key):
    """ Remove an item from the cart """
    try:
        product_id, size_id = (
            item_key.split('_') if '_' in item_key else (item_key, None)
            )
        product = Product.objects.get(pk=product_id)
        product_name = product.name  # Get product name
        cart = request.session.get('cart', {})

        if item_key in cart:
            del cart[item_key]
            request.session['cart'] = cart
            messages.success(
                request,
                f'{product_name} successfully removed from your cart.'
            )
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')

    return redirect('view_cart')
