class Shop:
    def __init__(self, name, itmes):
        self.name = name
        self.items = itmes

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Peaches"])
print(shop.get_items_count())
