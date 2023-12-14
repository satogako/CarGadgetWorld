from django.contrib import admin
from .models import Category, Brand, Catalogue, Image, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'sku', 'brand', 'category', 'auto_brand', 'stock', 'price'
    )

    ordering = ("sku",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Catalogue)
