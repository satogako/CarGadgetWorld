from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    Display for all products, including sorting and searching
    """
    products = Product.objects.all()

    context = {"products": products}
    return render(request, "products/products.html", context)
