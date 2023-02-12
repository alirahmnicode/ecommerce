from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ecommerce.inventory.urls", namespace="inventory")),
    path("demo/", include("ecommerce.demo.urls", namespace="demo")),
    path("cart/", include("ecommerce.cart.urls", namespace="cart")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
