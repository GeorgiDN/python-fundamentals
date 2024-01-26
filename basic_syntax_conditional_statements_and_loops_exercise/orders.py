num_orders = int(input())
total = 0.0

for order in range(num_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100.00:
        continue

    if 1 > days or days > 31:
        continue
    
    if 1 > capsules_per_day or capsules_per_day > 2000:
        continue

    order_total = capsules_per_day * price_per_capsule * days
    print(f"The price for the coffee is: ${order_total:.2f}")
    total += order_total

print(f"Total: ${total:.2f}")



# orders_num = int(input())
# total_price = 0

# for i in range(orders_num):
#     price_per_capsule = float(input())
#     days = int(input())
#     capsules_per_day = int(input())
#     if (price_per_capsule > 100 or price_per_capsule < 0.01)\
#         or (days > 31 or days < 1)\
#             or (capsules_per_day > 2000 or capsules_per_day < 1):
#         continue

#     price_for_coffee = price_per_capsule * days * capsules_per_day
#     total_price += price_for_coffee
#     print(f"The price for the coffee is: ${price_for_coffee:.2f}")

# print(f"Total: ${total_price:.2f}")
