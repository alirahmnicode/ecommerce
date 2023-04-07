from django.urls import path

from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_detail_view, name="cart_detail"),
    path(
        "add/<int:product_id>/<int:quantity>/",
        views.add_to_cart_view,
        name="add",
    ),
    path("remove/<int:product_id>/", views.remove, name="remove"),
    path("clear/", views.clear_cart, name="clear"),
]
