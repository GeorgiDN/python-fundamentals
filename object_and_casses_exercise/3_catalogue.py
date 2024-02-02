class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [letter for letter in self.products if letter.startswith(first_letter)]

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted([item for item in self.products]))
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)





# class Catalogue:
#     def __init__(self, name: str):
#         self.name = name
#         self.products = []

#     def add_product(self, product_name: str):
#         self.products.append(product_name)

#     def get_by_letter(self, first_letter: str):
#         filtered_products = [product for product in self.products if product.startswith(first_letter)]
#         return filtered_products

#     def __repr__(self):
#         sorted_products = sorted(self.products)
#         products_str = '\n'.join(sorted_products)
#         return f"Items in the {self.name} catalogue:\n{products_str}"


# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
