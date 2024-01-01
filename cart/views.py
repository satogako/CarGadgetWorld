from django.shortcuts import render, redirect
from django.urls import reverse


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

    cart = request.session.get('cart', {})
  
    if quantity > 0 and quantity < 100:
            cart[item_id] = quantity
    else:
         cart[item_id] = 1
    
    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))
