from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from ecommerce.inventory.models import ProductInventory

from .cart import Cart


# Create your views here.
def cart_detail_view(request):
    cart = Cart(request=request)
    for i in cart:
        print(i)
    return render(request, "cart/cart.html", {"cart": cart})


def add_to_cart_view(request, product_id, quantity):
    cart = Cart(request)
    product = get_object_or_404(ProductInventory, id=product_id)

    cart.add(product=product, quantity=quantity)

    return JsonResponse({"cart": request.session.get("cart")})


def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductInventory, id=product_id)

    cart.remove(product=product)

    return JsonResponse({"delete": True, "cart": cart})


def clear_cart(request):
    cart = Cart(request=request)
    cart.clear()
    return JsonResponse({"clear": True})
