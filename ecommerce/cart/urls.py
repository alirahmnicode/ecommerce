from django.urls import path

from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart, name="cart"),
    path(
        "quantity/<int:product_id>/<str:action>/",
        views.product_quantity,
        name="quantity",
    ),
    path("remove/<int:product_id>/", views.remove, name="remove"),
]
