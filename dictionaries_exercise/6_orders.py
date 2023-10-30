command = input()
my_dictionary = {}

while command != 'buy':
    products = command.split(' ')

    product = products[0]
    price = float(products[1])
    quantity = int(products[2])

    if product not in my_dictionary:
        my_dictionary[product] = {'price': price, 'quantity': quantity}
    else:
        my_dictionary[product]['quantity'] += quantity
        if my_dictionary[product]['price'] != price:
            my_dictionary[product]['price'] = price

    command = input()

for product, data in my_dictionary.items():
    total_price = data['price'] * data['quantity']
    print(f"{product} -> {total_price:.2f}")
  
