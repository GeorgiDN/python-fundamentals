def is_valid_quantity(num):
    return 0 < num


def receive_food(food_data_, qty, food):
    if is_valid_quantity(qty):
        if food not in food_data_:
            food_data_[food] = 0
        food_data_[food] += qty
    return food_data_


def sell_food(food_data_, qty, food, sold_food_):
    if food not in food_data_:
        print(f"You do not have any {food}.")
    else:
        sold_quantity = qty
        if food_data_[food] < qty:
            sold_quantity = food_data_[food]
            print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
        else:
            print(f"You sold {sold_quantity} {food}.")

        food_data_[food] -= sold_quantity
        if food_data_[food] <= 0:
            del food_data_[food]

        if food not in sold_food_:
            sold_food_[food] = 0
        sold_food_[food] += sold_quantity

    return food_data_, sold_food_


def print_result(food_data_, sold_food_):
    result = ''
    result += ''.join(map(str, (f"{f}: {q}\n" for f, q in food_data_.items())))

    number_sold_foods = sum(sold_food_.values())
    result += f"All sold: {number_sold_foods} goods"
    return print(result)


def main():
    food_data = {}
    sold_food = {}

    while True:
        command = input()
        if command == "Complete":
            break

        data = command.split()
        command = data[0]
        quantity, current_food = int(data[1]), data[2]

        if command == "Receive":
            food_data = receive_food(food_data, quantity, current_food)

        elif command == "Sell":
            food_data, sold_food = sell_food(food_data, quantity, current_food, sold_food)

    print_result(food_data, sold_food)


if __name__ == '__main__':
    main()
