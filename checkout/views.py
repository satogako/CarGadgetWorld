from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib import messages
from django.conf import settings

from .forms import PurchaseForm
from .models import Purchase, PurchaseLineItem
from products.models import Product
from cart.contexts import cart_contents

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'phone': request.POST['phone'],
            'email_addres': request.POST['email_addres'],
            'country': request.POST['country'],
            'full_address': request.POST['full_address'],
            'town_city': request.POST['town_city'],
            'post_code': request.POST['post_code'],
            'order_notes': request.POST['order_notes'],
        }
        order_form = PurchaseForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(quantity, int):
                        order_line_item = PurchaseLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found \
                            in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shopping_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('check_success', args=[order.order_number])
            )
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})

        if not cart:
            messages.error(
                request, "There's nothing in your bag at the moment"
            )
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = PurchaseForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                          Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_achievement(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Purchase, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_achieve.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
