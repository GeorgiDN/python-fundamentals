def total(product, number):
    result = None

    if product == 'coffee':
        result = 1.50 * number
    elif product == 'water':
        result = 1.00 * number
    elif product == 'coke':
        result = 1.40 * number
    elif product == 'snacks':
        result = 2.00 * number
    return f'{result:.2f}'


current_product = input()
current_number = int(input())


print(total(current_product, current_number))
