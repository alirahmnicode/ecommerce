from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path("", views.index, name="index"),
    path("product/detail/<slug:slug>/", views.product_detail, name="detail"),
    path("products/filter/", views.products_filter, name="filter"),
]
