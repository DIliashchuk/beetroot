class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = []

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        product.price *= 1.3  # Apply a 30% price premium for the store
        self.products.append({"product": product, "amount": amount})

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type not in ('name', 'type'):
            raise ValueError("Invalid identifier_type")
        for item in self.products:
            if (identifier_type == 'name' and item["product"].name == identifier) or \
               (identifier_type == 'type' and item["product"].type == identifier):
                item["product"].price *= (100 - percent) / 100

    def sell_product(self, product_name, amount):
        for item in self.products:
            if item["product"].name == product_name:
                if item["amount"] >= amount:
                    item["amount"] -= amount
                    return
                else:
                    raise ValueError("Not enough products in stock")
        raise ValueError("Product not found")

    def get_income(self):
        return sum((item["product"].price * (1 - 0.3) * item["amount"]) for item in self.products)

    def get_all_products(self):
        return [(item["product"].type, item["product"].name, item["amount"]) for item in self.products]

    def get_product_info(self, product_name):
        for item in self.products:
            if item["product"].name == product_name:
                return (item["product"].name, item["amount"])
        raise ValueError("Product not found")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)


s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)


print(s.get_product_info('Ramen'))
