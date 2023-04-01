from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from . import models
from .filters import ProductFiler
from .sort import Sort
from .utils import random_choice_list


# Create your views here.
def index(request):
    brands = models.Brand.objects.all()
    brands_list = random_choice_list(list(brands), 3)
    new_products = models.ProductInventory.objects.all()
    best_selling = new_products.order_by("-stock__units_sold")
    data = {
        "brands": brands_list,
        "new_products": new_products,
        "best_selling": best_selling,
    }
    return render(request, "inventory/index.html", {"data": data})


def product_detail(request, slug):

    product = (
        models.ProductInventory.objects.filter(product__slug=slug)
        .filter(is_default=True)
        .values(
            "id",
            "product__name",
            "product__description",
            "store_price",
            "brand__name",
            "brand__id",
            "product__category__name",
            "product__category__id",
            "stock__units",
            "stock__units_sold",
        )
        .get()
    )
    # get 20 similar products by category
    similar_products = models.ProductInventory.objects.filter(
        product__category__id=product["product__category__id"]
    )[:20]
    print(similar_products)
    context = {"product": product, "similar_products": similar_products}
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
