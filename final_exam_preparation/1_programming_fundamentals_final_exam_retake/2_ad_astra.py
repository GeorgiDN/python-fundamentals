#https://judge.softuni.org/Contests/Practice/Index/2525#1

import re


def extract_matches_and_calculate_total_calories(food_items_data, matches, total_calories):
    for match in matches:
        product = match.group(2)
        expiration_date = match.group(3)
        calories = int(match.group(4))
        total_calories += calories
        food_items_data += f"Item: {product}, Best before: {expiration_date}, Nutrition: {calories}\n"
    return food_items_data, total_calories


def print_result(food_items_data, calories_for_days):
    result = ''
    result += f"You have food to last you for: {calories_for_days} days!\n"
    result += food_items_data
    return print(result)


def main():
    text = input()
    pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(0|\d{1,4}|10000)\1'
    matches = re.finditer(pattern, text)
    needed_calories_per_day = 2000
    total_calories = 0
    food_items_data = ''

    food_items_data, total_calories = extract_matches_and_calculate_total_calories(food_items_data, matches, total_calories)
    calories_for_days = total_calories // needed_calories_per_day
    print_result(food_items_data, calories_for_days)


if __name__ == "__main__":
    main()




# import re
# 
# text = input()
# pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2})/(\d{2})/(\d{2})\1(0|\d{1,4}|10000)\1'
# matches = re.finditer(pattern, text)
# needed_calories_per_day = 2000
# total_calories = 0
# result = ''
# 
# for match in matches:
#     product = match.group(2)
#     day = match.group(3)
#     month = match.group(4)
#     year = match.group(5)
#     calories = int(match.group(6))
#     total_calories += calories
#     result += f"Item: {product}, Best before: {day}/{month}/{year}, Nutrition: {calories}\n"
# 
# calories_for_days = total_calories // needed_calories_per_day
# 
# print(f"You have food to last you for: {calories_for_days} days!")
# print(result)




# import re

# info = input()

# pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+|[1-9]\d{0,3}|10000)\1"

# matches = re.finditer(pattern, info)

# total_calories = 0
# food_items = []

# for match in matches:
#     item = match.group(2)
#     expiration_date = match.group(3)
#     calories = match.group(4)
#     total_calories += int(calories)
#     food_items.append((item, expiration_date, calories))

# calories_per_day = 2000
# calories_for_days = total_calories // calories_per_day

# print(f"You have food to last you for: {calories_for_days} days!")

# for item_info in food_items:
#     item, expiration_date, calories = item_info
#     print(f"Item: {item}, Best before: {expiration_date}, Nutrition: {calories}")
