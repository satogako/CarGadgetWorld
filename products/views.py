from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from django.contrib import messages
from .models import Product, Category, Brand


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
        brand_auto = self.kwargs.get('brand_auto')
        product_brand = self.kwargs.get('product_brand')
        query = self.request.GET.get('search', None)
        sort = self.request.GET.get('sort')
        order = self.request.GET.get('order')

        if category:
            queryset = queryset.filter(
                category__name=category).distinct()
        
        if brand_auto: 
            queryset = queryset.filter(
                auto_brand__auto_brand=brand_auto).distinct()
            
        if product_brand:
            queryset = queryset.filter(
                brand__name=product_brand).distinct()

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = self.kwargs.get('category')
        auto_brand = self.kwargs.get('brand_auto')
        product_brand = self.kwargs.get('product_brand')
        
        query = self.request.GET.get('search', None)

        sort = self.request.GET.get('sort')
        order = self.request.GET.get('order')

        if sort == 'name':
            if order == 'asc':
                context['sort_selected'] = 'Name (A-Z)'
            else:
                context['sort_selected'] = 'Name (Z-A)'
        elif sort == 'price':
            if order == 'asc':
                context['sort_selected'] = 'Price (Low to High)'
            else:
                context['sort_selected'] = 'Price (High to Low)'
        elif sort == 'date_added':
            if order == 'asc':
                context['sort_selected'] = 'Oldest First'
            else:
                context['sort_selected'] = 'Newest First'

        context['category'] = get_object_or_404(
            Category, name=category) if category else None
        
        context['auto_brand_name'] = auto_brand

        context['product_brand_name'] = get_object_or_404(
                 Brand, name=product_brand) if product_brand else None

        context['search_results'] = query

        return context
    

def product_detail(request, slug):
    ''''
    Displays detailed information about a single product
    '''
    product = get_object_or_404(Product, slug=slug)

    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
