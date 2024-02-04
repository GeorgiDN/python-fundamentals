products_with_quantity = {}

while True:
    information = input()
    if information == "statistics":
        break

    data = information.split(": ")
    product, quantity = data[0], int(data[1])
    if product not in products_with_quantity:
        products_with_quantity[product] = quantity
    else:
        products_with_quantity[product] += quantity

total_products = len(products_with_quantity)
total_quantity = sum([val for val in products_with_quantity.values()])

print(f"Products in stock:")
print('\n'.join([f"- {key}: {val_}" for key, val_ in products_with_quantity.items()]))
print(f"Total Products: {total_products}\n"
      f"Total Quantity: {total_quantity}")




# products = {}

# command = input()

# while command != 'statistics':

#     tokens = command.split(": ")
#     product = tokens[0]
#     quantity = int(tokens[1])

#     if product not in products:
#         products[product] = 0
#     products[product] += quantity
#     command = input()
# print(f"Products in stock:")
# for (product, quantity) in products.items():
#     print(f"- {product}: {quantity}")

# print(f"Total Products: {len(products.keys())}")
# print(f"Total Quantity: {sum(products.values())}")
