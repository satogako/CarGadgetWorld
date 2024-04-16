from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WishList
from products.models import Product
from django.contrib import messages


@login_required
def view_wish_list(request):
    '''
    Displays user's wish list page.
    '''
    wish_list, created = WishList.objects.get_or_create(user=request.user)
    products = wish_list.products.all()
    context = {
        'wishlist_products': products
    }
    return render(request, 'wish_list/wish_list.html', context)


def add_to_wish_list(request, product_id):
    '''
    Adds product to user's wish list, showing success/info messages based on
    the product's presence in the list or user authentication status.
    '''
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        wish_list, created = WishList.objects.get_or_create(user=request.user)

        if product in wish_list.products.all():
            messages.info(
                request, f'The {product.name} has already been added to your \
                    Wish List page.'
            )
        else:
            wish_list.products.add(product)
            messages.success(
                    request, f'Added {product.name} to your Wish List page.'
            )
        return redirect(request.META.get('HTTP_REFERER', 'wish_list'))
    else:
        messages.info(
            request, 'Please signup or login to unlock the ability '
            'to add items to your Wish List page.'
        )
        return redirect('account_signup')


@login_required
def remove_from_wish_list(request, product_id):
    '''
    Removes a product from the user's wish list and redirects to
    the wish list page.
    '''
    product = get_object_or_404(Product, id=product_id)
    wish_list = WishList.objects.get(user=request.user)
    wish_list.products.remove(product)
    messages.success(
        request, f'Removed {product.name} from your your Wish List page.'
    )
    return redirect('wish_list')
