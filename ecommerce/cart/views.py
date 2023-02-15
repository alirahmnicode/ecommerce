from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def cart(request):
    cart = request.session.get("cart")
    return render(request, "cart/cart.html", {"cart": cart})
