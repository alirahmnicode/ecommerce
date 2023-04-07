from django.urls import path

from .views import check_reault_payment, payment_process

app_name = "payment"

urlpatterns = [
    path("process/", payment_process, name="process"),
    path("result/", check_reault_payment, name="result"),
]
