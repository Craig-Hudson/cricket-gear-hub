from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' : 
        'pk_test_51P6V2QRunzMTc6Q0D6EQMnI3wGwSQORfPhQZcTWLZB8UvgoKweaJOi1XVntS3cWURHB13F7JcjMeOIT1YVKoiPud00yRWFJ1VI',
        'client_secret' : 'test client secret'
    }

    return render(request, template, context)