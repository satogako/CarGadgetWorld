from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from django.contrib import messages
from .models import Product

class ProductsList(generic.ListView):
    '''
    Displays all products, performs sorting and searching
    '''
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()

        category = self.kwargs.get('category')
        query = self.request.GET.get('search', None)
        sort = self.request.GET.get('sort')
        order = self.request.GET.get('order')

        if category:
            queryset = queryset.filter(
                category__name=category).distinct()

        if query:
            queryset = queryset.filter(name__icontains=query
                                    ).distinct() | queryset.filter(
                description__icontains=query).distinct()

        elif query == '':
            messages.error(self.request,
                        "You didn't enter any search criteria.")

            queryset = queryset.none()

        if sort == 'name':
            if order == 'asc':
                queryset = queryset.order_by('name')
            else:
                queryset = queryset.order_by('-name')
        elif sort == 'price':
            if order == 'asc':
                queryset = queryset.order_by('price')
            else:
                queryset = queryset.order_by('-price')

        return queryset
    

def product_detail(request, slug):
    ''''
    Displays detailed information about a single product
    '''
    product = get_object_or_404(Product, slug=slug)

    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
