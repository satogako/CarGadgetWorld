from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Product


def all_products(request):
    """
    Display for all products, including sorting and searching
    """
    products = Product.objects.all()

    context = {"products": products}
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """
    Displays more detailed information about a specific product
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {"product": product}
    return render(request, "products/product_detail.html", context)
