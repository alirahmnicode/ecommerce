from django.urls import path

app_name = "orders"

from .views import order_create_view

urlpatterns = [
    path("create/", order_create_view, name="create"),
]
