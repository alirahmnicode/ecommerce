from django.http import JsonResponse
from django.shortcuts import render

from .cart import Cart


# Create your views here.
def cart(request):
    cart = request.session.get("cart")
    return render(request, "cart/cart.html", {"cart": cart})


def product_quanity(request, product_id, action):
    cart = Cart(request)
    if action == "add":
        cart.add(product_id)
    else:
        cart.reduce(product_id)
    return JsonResponse({"cart": request.session.get("cart")})
