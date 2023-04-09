from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ecommerce.inventory.urls", namespace="inventory")),
    path("cart/", include("ecommerce.cart.urls", namespace="cart")),
    path("user/", include("ecommerce.account.urls", namespace="user")),
    path("orders/", include("ecommerce.orders.urls", namespace="orders")),
    path("payment/", include("ecommerce.payment.urls", namespace="payment")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
