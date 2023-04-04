from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(_("First Name:"), max_length=225)
    last_name = models.CharField(_("Last Name:"), max_length=225)
    address = models.CharField(_("Address"), max_length=1000)

    order_notes = models.CharField(_("Order Notes"), max_length=700, blank=True)

    datetime_created = models.DateTimeField(_("Created"), auto_now_add=True)
    datetime_modified = models.DateTimeField(_("Modified"), auto_now=True)

    def __str__(self) -> str:
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        "inventory.ProductInventory",
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"OrderItem {self.id}: {self.product} x {self.quantity} (price:{self.price})"
