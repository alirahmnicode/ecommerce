from ecommerce.inventory.models import ProductInventory


class Cart:
    def __init__(self, request, product_id: int) -> None:
        self.session = request.session
        self.product_id = product_id
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

        products = self.cart.get("products")
        if not products:
            products = self.cart["products"] = {}
        self.products = products

    def add(self):
        # add new product to products
        product_id = str(self.product_id)
        if product_id in self.products.keys():
            self.products[product_id]["quantity"] += 1
        else:
            self.products[product_id] = {"quantity": 1, "product": self.get_product()}
        # update total price
        self.cart["total_price"] = self.get_total_price()
        self.save()

    def get_total_price(self):
        total_price = 0
        total_price = sum(
            [
                p["quantity"] * p["product"]["store_price"]
                for p in self.products.values()
            ]
        )
        return total_price

    def get_product(self):
        product = ProductInventory.objects.filter(id=self.product_id).values(
            "product__name", "store_price"
        )
        product_price = list(product)[0]["store_price"]
        list(product)[0]["store_price"] = float(product_price)
        return list(product)[0]

    def save(self):
        self.session.modified = True
