bought_item_list = input().split('|')
budget = float(input())

new_bough_item_list = []
profit = 0
total_sum = 0

for item in bought_item_list:
    item_info = item.split("->")
    item_type = item_info[0]
    item_value = float(item_info[1])

    if item_type == 'Clothes' and item_value <= 50:
        if item_value <= budget:
            budget -= item_value
            new_bough_item_list.append(item_value)

    elif item_type == 'Shoes' and item_value <= 35:
        if item_value <= budget:
            budget -= item_value
            new_bough_item_list.append(item_value)

    elif item_type == 'Accessories' and item_value <= 20.50:
        if item_value <= budget:
            budget -= item_value
            new_bough_item_list.append(item_value)

for price in new_bough_item_list:
    increased_item_value = price * 1.40
    total_sum += increased_item_value
    profit += increased_item_value - price
    print(f'{increased_item_value:.2f}',end=' ')
print()

print(f'Profit: {profit:.2f}')

if (total_sum + budget) >= 150:
     print('Hello, France!')
else:
    print('Not enough money.')
