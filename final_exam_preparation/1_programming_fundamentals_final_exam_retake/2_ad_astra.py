#https://judge.softuni.org/Contests/Practice/Index/2525#1
import re

info = input()

pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+|[1-9]\d{0,3}|10000)\1"

matches = re.finditer(pattern, info)

total_calories = 0
food_items = []

for match in matches:
    item = match.group(2)
    expiration_date = match.group(3)
    calories = match.group(4)
    total_calories += int(calories)
    food_items.append((item, expiration_date, calories))

calories_per_day = 2000
calories_for_days = total_calories // calories_per_day

print(f"You have food to last you for: {calories_for_days} days!")

for item_info in food_items:
    item, expiration_date, calories = item_info
    print(f"Item: {item}, Best before: {expiration_date}, Nutrition: {calories}")
