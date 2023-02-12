import pprint

from django.shortcuts import render

from . import models


# Create your views here.
def index(request):
    categories = models.Category.objects.all()[:10]
    brands = models.Brand.objects.all()[:4]
    new_products = models.ProductInventory.objects.all()
    discount_products = list(new_products)[:4]
    data = {
        "categories": categories,
        "brands": brands,
        "new_products": new_products,
        "discount_products": discount_products,
    }
    return render(request, "inventory/index.html", {"data": data})


def product_detail(request, slug):

    from django.contrib.postgres.aggregates import ArrayAgg

    product = (
        models.ProductInventory.objects.filter(product__slug=slug)
        .filter(is_default=True)
        .values(
            "id",
            "sku",
            "product__name",
            "product__description",
            "store_price",
            "product_inventory__units",
            "brand",
        )
        .annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
        .get()
    )
    y = (
        models.ProductInventory.objects.filter(product__slug=slug)
        .distinct()
        .values(
            "attribute_values__product_attribute__name",
            "attribute_values__attribute_value",
        )
    )

    z = (
        models.ProductTypeAttribute.objects.filter(
            product_type__product_type__product__slug=slug
        )
        .distinct()
        .values("product_attribute__name")
    )
    pprint.pprint(product["field_a"])
    context = {"product": product, "filter": y, "z": z}
    return render(request, "inventory/product_detail.html", context)
