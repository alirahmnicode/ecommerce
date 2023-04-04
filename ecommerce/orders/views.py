from django.shortcuts import render

from .forms import OrderForm


def order_create_view(request):
    if request.method == "POST":
        pass
    form = OrderForm()
    return render(request, "orders/create.html", {"form": form})
