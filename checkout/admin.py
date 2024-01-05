from django.contrib import admin
from .models import Purchase, PurchaseLineItem


class PurchaseLineItemAdminInline(admin.TabularInline):
    model = PurchaseLineItem
    readonly_fields = ('lineitem_total',)


class PurchaseAdmin(admin.ModelAdmin):
    inlines = (PurchaseLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'first_name', 'last_name',
              'email_addres', 'phone', 'country',
              'full_address', 'town_city', 'post_code', 'order_notes',
              'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Purchase, PurchaseAdmin)
