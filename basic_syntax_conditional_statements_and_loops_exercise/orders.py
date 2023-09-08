orders_num = int(input())
total_price = 0

for i in range(orders_num):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if (price_per_capsule > 100 or price_per_capsule < 0.01)\
        or (days > 31 or days < 1)\
            or (capsules_per_day > 2000 or capsules_per_day < 1):
        continue

    price_for_coffee = price_per_capsule * days * capsules_per_day
    total_price += price_for_coffee
    print(f"The price for the coffee is: ${price_for_coffee:.2f}")

print(f"Total: ${total_price:.2f}")
