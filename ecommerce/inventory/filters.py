import django_filters

from .models import ProductInventory


class ProductFiler(django_filters.FilterSet):
    class Meta:
        model = ProductInventory
        fields = ["brand", "product__category"]
