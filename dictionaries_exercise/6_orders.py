def orders_task():
    products_info = {}
    while True:
        command = input()
        if command == "buy":
            break

        info = command.split()

        product, price, quantity = info[0], float(info[1]), int(info[2])
        if product not in products_info:
            products_info[product] = [price, quantity]
        else:
            if price != products_info[product][0]:
                products_info[product][0] = price
            products_info[product][1] += quantity

    result = []
    for name, data in products_info.items():
        price_ = data[0]
        qty = data[1]
        total_price = price_ * qty
        result.append(f"{name} -> {total_price:.2f}")

    return print('\n'.join(result))


orders_task()




# products_info = {}
#
# while True:
#     command = input()
#     if command == 'buy':
#         break
#     products = command.split(' ')
#
#     product = products[0]
#     price = float(products[1])
#     quantity = int(products[2])
#
#     if product not in products_info:
#         products_info[product] = {'price': price, 'quantity': quantity}
#     else:
#         products_info[product]['quantity'] += quantity
#         if products_info[product]['price'] != price:
#             products_info[product]['price'] = price
#
#
# for product, data in products_info.items():
#     total_price = data['price'] * data['quantity']
#     print(f"{product} -> {total_price:.2f}")
