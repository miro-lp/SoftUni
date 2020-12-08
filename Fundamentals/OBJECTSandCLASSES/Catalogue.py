class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.product = product
        self.products.append(self.product)

    def get_by_letter(self, first_letter):
        self.first_letter = first_letter
        self.letter_products = [i for i in self.products if i[0] == self.first_letter]
        return self.letter_products

    def __repr__(self):
        self.products = sorted(self.products)
        result = f"Items in the {self.name} catalogue:\n"
        result += "\n".join(self.products)
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
