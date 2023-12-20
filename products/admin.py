from django.contrib import admin
from .models import Category, Brand, Catalogue, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'sku', 'brand', 'category', 'auto_brand', 'stock', 'image', 'price'
    )

    ordering = ("sku",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Catalogue)
