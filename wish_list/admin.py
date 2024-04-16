from django.contrib import admin
from django.utils.html import format_html
from .models import WishList


class WishListAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'get_products',
    )

    def get_products(self, obj):
        products_html = '<ul>'
        for product in obj.products.all():
            products_html += f'<li>{product.name}</li>'
        products_html += '</ul>'
        return format_html(products_html)
    get_products.short_description = 'Products'


admin.site.register(WishList, WishListAdmin)
