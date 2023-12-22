from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Product


class ProductsList(generic.ListView):
    '''
    Displays all products
    '''
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    

def product_detail(request, slug):
    ''''
    Displays detailed information about a single product
    '''
    product = get_object_or_404(Product, slug=slug)

    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
