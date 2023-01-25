from django.shortcuts import render
from ecommerce.inventory import models


def home(request):
    return render(request, "base.html")


def category(request):
    data = models.Category.objects.all()
    return render(request, "category.html", {"data": data})
