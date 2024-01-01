from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from products.models import Product


def view_cart(request):
    '''A view that renders the cart contents page'''

    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

  
def adjust_cart(request, item_id):
    '''Adjust the quantity of the specified product 
        to the specified amount
    '''
    try:
        quantity = int(request.POST.get('quantity'))
    except ValueError:
        quantity = 1
        messages.error(request, f'The number must be an integer')

    cart = request.session.get('cart', {})
  
    if quantity > 0 and quantity < 100:
            cart[item_id] = quantity
    else:
         cart[item_id] = 1
         messages.error(
            request, f'The quantity must be between 1 and 99'
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