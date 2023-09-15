lost_fights_count = int(input())

expenses = 0

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

for game in range(1, lost_fights_count + 1):
    if game % 2 == 0:
        expenses += helmet_price
        if game % 3 == 0:
            expenses += sword_price
            expenses += shield_price
            if game % 12 == 0:
                expenses += armor_price

    elif game % 3 == 0:
        expenses += sword_price

print(f"Gladiator expenses: {expenses:.2f} aureus")

