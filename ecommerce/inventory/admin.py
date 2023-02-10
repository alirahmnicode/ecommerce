from django.contrib import admin
from ecommerce.inventory.models import Category, Product, ProductInventory

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInventory)
