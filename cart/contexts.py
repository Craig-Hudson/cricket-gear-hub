from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Size

def cart_contents(request):
    cart_items = []
    total = Decimal('0')
    product_count = 0
    delivery = Decimal('3.99')
    cart = request.session.get('cart', {})

    for item_key, quantity in cart.items():
        if '_' in item_key:
            product_id, size_id = item_key.split('_')  # Split product ID and size ID
            product = get_object_or_404(Product, pk=product_id)
            size = get_object_or_404(Size, pk=size_id)  
        else:
            product = get_object_or_404(Product, pk=item_key)
            size = None

        subtotal_for_item = quantity * product.price  
        total += subtotal_for_item  
        product_count += quantity
        cart_items.append({
            'item_key': item_key,
            'quantity': quantity,
            'product': product,
            'size': size, 
            'subtotal': subtotal_for_item,
        })

    # Calculate grand total
    grand_total = total + delivery

    context = {
        'cart_items' : cart_items,
        'total' : total,
        'product_count' : product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
