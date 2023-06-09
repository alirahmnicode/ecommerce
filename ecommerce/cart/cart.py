from ecommerce.inventory.models import ProductInventory


class Cart:
    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session

        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductInventory.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product_obj"] = product

        for item in cart.values():
            item["total_price"] = item["product_obj"].store_price * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0}

        self.cart[product_id]["quantity"] += quantity

        self.save()

    def reduce(self, product):
        # reduce one item from cart
        product_id = str(product.id)
        for i in self.cart.keys():
            if product_id == i:
                quantity = self.cart[product_id]["quantity"]
                if quantity > 1:
                    self.cart[product_id]["quantity"] -= 1
                else:
                    self.remove(product)
                self.save()
                break

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session["cart"]
        self.save()

    def get_total_price(self):
        return sum(
            item["quantity"] * item["product_obj"].store_price
            for item in self.cart.values()
        )

    def get_total_quantity(self):
        return sum(item["quantity"] for item in self.cart.values())

    def save(self):
        self.session.modified = True

    def is_empty(self):
        if self.cart:
            return False
        return True
