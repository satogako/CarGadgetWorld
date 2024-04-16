from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from products.models import Product
from wish_list.models import WishList


def view_cart(request):
    '''A view that renders the cart contents page'''

    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}'
            )
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

        request.session['cart'] = cart

        """Сheck whether the request was made from the wishlist and if yes,
            removes the product from the Wish List page.
        """
        if 'wish_list' in redirect_url:
            wish_list = WishList.objects.get(user=request.user)
            wish_list.products.remove(product)
            messages.success(
                request, f'Removed {product.name} from your wish list'
            )

        return redirect(redirect_url)
    else:
        messages.info(
            request, 'Please signup or login to unlock the ability '
            'to make purchases.'
        )
        return redirect('account_signup')


def adjust_cart(request, item_id):
    '''Adjust the quantity of the specified product
        to the specified amount
    '''
    product = get_object_or_404(Product, pk=item_id)

    try:
        quantity = int(request.POST.get('quantity'))
    except ValueError:
        quantity = 1
        messages.warning(request, f'The quantity must be an integer')

    cart = request.session.get('cart', {})

    if quantity < 1:
        cart[item_id] = 1
        messages.warning(
            request, f"The quantity can't be less than 1"
        )

    elif quantity < 100:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
        )
    else:
        cart[item_id] = 1
        messages.info(
            request, f'The quantity must be less 100'
        )

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
