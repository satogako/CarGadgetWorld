from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import PurchaseForm


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = PurchaseForm()
    template = 'checkout/checkout.html'
    
    context = {
        'order_form': order_form,
    }
    
    return render(request, template, context)
