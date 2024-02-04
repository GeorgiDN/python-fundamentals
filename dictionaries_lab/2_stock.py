products_and_quantity = input().split(" ")
products_with_quantity = {products_and_quantity[i]: int(products_and_quantity[i + 1])
                          for i in range(0, len(products_and_quantity), 2)}

check_products = input().split(" ")

print('\n'.join([f"We have {products_with_quantity[product]} of {product} left" if product in products_with_quantity
                 else f"Sorry, we don't have {product}" for product in check_products]))




# elements = input().split(" ")
# bakery = {}

# for i in range(0, len(elements), 2):
#     key = elements[i]
#     value = elements[i + 1]
#     bakery[key] = int(value)

# searched_products = input().split(" ")
# for product in searched_products:
#     if product in bakery:
#         print(f"We have {bakery[product]} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")
