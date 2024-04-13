from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Purchase, PurchaseLineItem
from products.models import Product

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, purchase):
        """Send the user a confirmation email"""
        cust_email = purchase.email_addres
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'purchase': purchase})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'purchase': purchase,
                'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Purchase.objects.get(
                    first_name__iexact=shipping_details.name.split(' ', 1)[0],
                    last_name__iexact=shipping_details.name.split(' ', 1)[1],
                    email_addres__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    post_code__iexact=shipping_details.address.postal_code,
                    town_city__iexact=shipping_details.address.city,
                    full_address__iexact=shipping_details.address.line1,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )

                order_exists = True
                break

            except Purchase.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | \
                        SUCCESS Verified order olready in database',
                            status=200)
        else:
            order = None
            try:
                order = Purchase.objects.create(
                        first_name=shipping_details.name.split(' ', 1)[0],
                        last_name=shipping_details.name.split(' ', 1)[1],
                        email_addres=billing_details.email,
                        phone=shipping_details.phone,
                        country=shipping_details.address.country,
                        post_code=shipping_details.address.postal_code,
                        town_city=shipping_details.address.city,
                        full_address=shipping_details.address.line1,
                        original_cart=cart,
                        stripe_pid=pid,
                    )
                for item_id, quantity in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(quantity, int):
                        order_line_item = PurchaseLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | \
            SUCCES: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
