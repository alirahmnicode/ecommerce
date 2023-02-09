from django.shortcuts import render

from . import models


# Create your views here.
def index(request):
    categories = models.Category.objects.all()[:10]
    brands = models.Brand.objects.all()[:4]
    shoes = models.Product.objects.filter(category__name="comfort")[:4]
    data = {"categories": categories, "brands": brands}
    return render(request, "inventory/index.html", {"data": data})
