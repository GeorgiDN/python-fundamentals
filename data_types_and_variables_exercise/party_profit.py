group_size = int(input())
days_adventure = int(input())

coins_total = 0

for day in range(1, days_adventure + 1):
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins_total += 50 - 2 * group_size

    if day % 3 == 0:
        coins_total -= 3 * group_size

    if day % 5 == 0:
        coins_total += 20 * group_size
        if day % 3 == 0:
            coins_total -= 2 * group_size

print(f'{group_size} companions received {coins_total // group_size} coins each.')
