from django.db.models import Count
from ecommerce.inventory.models import ProductInventory


class Cart:
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

        products = self.cart.get("products")
        if not products:
            products = self.cart["products"] = {}
        self.products = products

    def add(self, product_id):
        product_id = str(product_id)
        if product_id in self.products.keys():
            # update quantity and item price
            product = self.products[product_id]["product"]
            product["quantity"] += 1
            self.set_item_price(product, product_id)
        else:
            # add new item to cart
            product = self.get_product(product_id)
            self.products[product_id] = {
                "product": product,
                "item_price": product["store_price"],
            }
        # update total price
        self.get_total_price()
        self.save()

    def reduce(self, product_id):
        product_id = str(product_id)
        product = self.products[product_id]["product"]
        product["quantity"] -= 1
        if product["quantity"] == 0:
            del self.products[product_id]
        else:
            self.set_item_price(product, product_id)
        self.get_total_price()
        self.save()

    def set_item_price(self, product, product_id):
        item_price = product["store_price"] * product["quantity"]
        self.products[product_id]["item_price"] = item_price

    def get_total_price(self):
        total_price = 0
        total_price = sum(
            [
                p["product"]["quantity"] * p["product"]["store_price"]
                for p in self.products.values()
            ]
        )
        self.cart["total_price"] = total_price

    def get_product(self, product_id):
        product = (
            ProductInventory.objects.filter(id=product_id)
            .values("product__name", "store_price")
            .annotate(quantity=Count(1))
        )[0]
        product_price = product["store_price"]
        product["store_price"] = float(product_price)
        return product

    def save(self):
        self.session.modified = True
