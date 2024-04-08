from django.shortcuts import render, redirect
from django.contrib import messages


def view_cart(request):
    """ A view to render the cart page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    size_id = request.POST.get('size')  # Get the selected size ID
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Create a unique key for each item based on product ID and size ID
    item_key = f"{item_id}_{size_id}" if size_id else str(item_id)


    if item_key in cart:
        cart[item_key] += quantity
    else:
        cart[item_key] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_key):
    """ Update the quantity of an item in the cart """
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        cart[item_key] = quantity
        request.session['cart'] = cart
        messages.success(request, 'Cart updated successfully.')
    return redirect('view_cart')

def remove_from_cart(request, item_key):
    """ Remove an item from the cart """

    cart = request.session.get('cart', {})

    if item_key in cart:
        del cart[item_key]
        request.session['cart'] = cart

    return redirect('view_cart')
