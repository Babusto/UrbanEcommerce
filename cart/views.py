from django.shortcuts import render

from django.conf import settings
from django.contrib.auth.decorators import login_required


from .cart import Cart

from product.models import Product

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')
