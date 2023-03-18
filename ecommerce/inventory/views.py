from django.core.paginator import Paginator
from django.http import JsonResponse
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
    )
    context = {"product": product}
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


def search(request):
    query = request.GET.get("q")
    template = request.GET.get("template")

    if query:
        # search
        products = models.Product.objects.filter(name__icontains=query).values(
            "name",
            "slug",
            "product__store_price",
            "id",
        )
        categories = models.Category.objects.filter(name__icontains=query).values(
            "name",
            "id",
        )
        data = {"products": list(products)[:4], "categories": list(categories)[:4]}
    else:
        data = {}
        products = []

    if template:
        p = Paginator(products, 20)
        page_number = request.GET.get("page")
        page_obj = p.get_page(page_number)
        return render(request, "inventory/search_result.html", {"objects": page_obj})
    else:
        return JsonResponse(data=data)
