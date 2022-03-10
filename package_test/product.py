data = [
    {"name": "Pizza Margherita", "nutriscore": "D", "kcal_100g": 888.4},
    {"name": "Nutella", "kcal_100g": 688.4, "nutriscore": "E"},
    {"name": "Coca", "kcal_100g": 1888.4, "nutriscore": "F"},
    {"name": "Pizza Calzone", "kcal_100g": 788.4, "nutriscore": "C"},
]


class Product:

    def __init__(self, name, nutriscore, **kwargs):
        self.name = name
        self.nutriscore = nutriscore

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"Product(name={self.name}, nutriscore={self.nutriscore})"


def create_products(data):
    list_of_products = []
    for product in data:
        p = Product(**product)
        list_of_products.append(p)
    return list_of_products


products = create_products(data)
print(products)
