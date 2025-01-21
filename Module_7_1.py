class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return file.read().strip()

    def add(self, *products):
        existing_products = set()

        try:
            with open(self.__file_name, 'r+', encoding='utf-8') as file:
                for line in file:
                    product_data = line.strip().split(', ')
                    existing_products.add(product_data[0])

                for product in products:
                    if product.name not in existing_products:
                        file.write(f"\n{product}")
                        print(f"{product}")
                    else:
                        print(f"Продукт {product.name} уже есть в магазине")
        except FileNotFoundError:
            with open(self.__file_name, 'w', encoding='utf-8') as file:
                for product in products:
                    file.write(f"{product}\n")

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')



print(p2) # __str__



s1.add(p1, p2, p3)



print(s1.get_products())