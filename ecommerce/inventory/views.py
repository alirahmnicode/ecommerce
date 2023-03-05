from django.core.paginator import Paginator
from django.shortcuts import render

from . import models
from .filters import ProductFiler
from .sort import Sort


# Create your views here.
def index(request):
    brands = models.Brand.objects.all()[:4]
    new_products = models.ProductInventory.objects.all()
    discount_products = list(new_products)[:4]
    data = {
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
    context = {"product": product, "filter": y, "z": z}
    return render(request, "inventory/product_detail.html", context)


def products_filter(request):
    product = models.ProductInventory.objects.all()
    if request.GET.get("sort"):
        sort_field = request.GET.get("sort_field")
        ascending = request.GET.get("ascending")
        sort = Sort(product)
        product = sort.sort_by(sort_field, ascending)
    f = ProductFiler(request.GET, queryset=product)
    p = Paginator(f.qs, 20)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    context = {"filter": f, "objects": page_obj}
    return render(request, "inventory/filter.html", context)
