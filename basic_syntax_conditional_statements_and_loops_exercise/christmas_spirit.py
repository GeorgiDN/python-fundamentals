quantity_decoration = int(input())
days_left = int(input())

spirit_points = 0
total_cost = 0

for day in range(1, days_left + 1):
    if day % 2 == 0:
        total_cost += 2 * quantity_decoration
        spirit_points += 5
    if day % 3 == 0:
        total_cost += 8 * quantity_decoration
        spirit_points += 13
    if day % 5 == 0:
        total_cost += 15 * quantity_decoration
        spirit_points += 17
    if day % 10 == 0:
        quantity_decoration += 2  # Увеличаваме количеството преди да ги купим
        spirit_points -= 20
        total_cost += 23

if days_left == 10:
    spirit_points -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_points}")
