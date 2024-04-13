import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product


class Purchase(models.Model):
    order_number = models.CharField(max_length=40, null=False, editable=False)
    first_name = models.CharField(max_length=35, null=False, blank=False)
    last_name = models.CharField(max_length=35, null=False, blank=False)
    email_addres = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=25, null=False, blank=False)
    country = CountryField(
        blank_label='Country / Region*', null=False, blank=False
    )
    full_address = models.CharField(max_length=254, null=False, blank=False)
    town_city = models.CharField(max_length=35, null=False, blank=False)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    order_notes = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0
    )
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * (
                Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / Decimal(100)
                )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class PurchaseLineItem(models.Model):
    order = models.ForeignKey(
        Purchase, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
