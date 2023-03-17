from django.contrib import admin
from ecommerce.inventory.models import Category, Product, ProductInventory


class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name", "slug"]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInventory)
