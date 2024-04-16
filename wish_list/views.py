from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WishList
from products.models import Product
from django.contrib import messages


@login_required
def view_wish_list(request):
    wish_list, created = WishList.objects.get_or_create(user=request.user)
    products = wish_list.products.all()
    context = {
        'wishlist_products': products
    }
    return render(request, 'wish_list/wish_list.html', context)


def add_to_wish_list(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        wish_list, created = WishList.objects.get_or_create(user=request.user)
        wish_list.products.add(product)
        return redirect(request.META.get('HTTP_REFERER', 'wish_list'))
    else:
        messages.info(
            request, 'Please signup or login to unlock the ability '
            'to add items to your wishlist.'
        )
        return redirect('account_signup')

@login_required
def remove_from_wish_list(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wish_list = WishList.objects.get(user=request.user)
    wish_list.products.remove(product)
    return redirect('wish_list')