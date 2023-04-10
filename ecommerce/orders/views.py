from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ecommerce.cart.cart import Cart

from .forms import OrderForm
from .models import OrderItem


@login_required
def order_create_view(request):
    cart = Cart(request)
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item["product_obj"]
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item["quantity"],
                    price=product.store_price,
                )

            cart.clear()

            request.session["order_id"] = order_obj.id

            return redirect("payment:process")

    form = OrderForm()
    return render(request, "orders/create.html", {"form": form, "cart": cart})
