import json

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from ecommerce.orders.models import Order

from .constant import CALLBACK_URL, CREATE_PAYMENT, PAYMENT_URL, VEIYFY_URL


@login_required
def payment_process(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    user = request.user

    # urls
    base_url = CREATE_PAYMENT
    payment_url = PAYMENT_URL

    # request data
    requets_headers = {"Content-Type": "application/json"}
    request_data = {
        "merchant": "zibal",
        "amount": 100000,
        "callbackUrl": CALLBACK_URL,
        "orderId": order_id,
        "mobile": user.phone,
    }

    # create payment
    res = requests.post(
        url=base_url, data=json.dumps(request_data), headers=requets_headers
    ).json()

    result = res["result"]
    message = res["message"]

    # redirect to payment page and start payment
    if result == 100 or message == "success":
        return redirect(payment_url.format(trackId=res["trackId"]))
    else:
        return redirect("/")


@login_required
def check_reault_payment(request):
    success = request.GET.get("success")
    track_id = request.GET.get("trackId")
    order_id = request.GET.get("orderId")

    order = get_object_or_404(Order, id=order_id)

    if success == "1":
        # set order paid to true
        order_obj = order
        order_obj.is_paid = True
        order_obj.save()
        # verify payment
        # verify_url = VEIYFY_URL

        # requets_headers = {"Content-Type": "application/json"}
        # request_data = {
        #     "merchant": "zibal",
        #     "trackId": track_id,
        # }

        # res = requests.post(
        #     url=verify_url, headers=requets_headers, data=request_data
        # ).json()

        # message = res["message"]

        data = {
            "success": success,
            "track_id": track_id,
            "order": order,
            # "message": message,
        }

        return render(request, "payment/result.html", {"data": data})
