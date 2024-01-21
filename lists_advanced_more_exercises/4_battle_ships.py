rows = int(input())
field = [[int(x) for x in input().split(" ")] for _ in range(rows)]
coordinates_for_attack = input().split(" ")
destroyed_ships = 0

for attacking_number in coordinates_for_attack:
    row, column = int(attacking_number[0]), int(attacking_number[2])
    if field[row][column] > 0:
        field[row][column] -= 1
        if field[row][column] == 0:
            destroyed_ships += 1

print(destroyed_ships)
