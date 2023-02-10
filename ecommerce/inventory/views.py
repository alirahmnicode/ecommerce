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
