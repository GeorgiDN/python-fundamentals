def take_integer_input():
    return int(input())


def take_string_input():
    return input()


def fill_the_field(rows_number):
    return [[int(x) for x in take_string_input().split(" ")] for _ in range(rows_number)]


def take_coordinates_for_attack():
    return take_string_input().split(' ')


def increment_destroyed_ships(counter):
    return counter + 1


def battle_ships(matrix, coord_for_attack, ships_destroyed):
    for attacking_number in coord_for_attack:
        row, column = int(attacking_number[0]), int(attacking_number[2])
        if matrix[row][column] > 0:
            matrix[row][column] -= 1
            if matrix[row][column] == 0:
                ships_destroyed = increment_destroyed_ships(ships_destroyed)

    return matrix, coord_for_attack, ships_destroyed


def print_result(result):
    return print(result)


rows = take_integer_input()
field = fill_the_field(rows)
coordinates_for_attack = take_coordinates_for_attack()
destroyed_ships = 0
field, coordinates_for_attack, destroyed_ships = battle_ships(field, coordinates_for_attack, destroyed_ships)
print_result(destroyed_ships)




##
# rows = int(input())
# field = [[int(x) for x in input().split(" ")] for _ in range(rows)]
# coordinates_for_attack = input().split(" ")
# destroyed_ships = 0

# for attacking_number in coordinates_for_attack:
#     row, column = int(attacking_number[0]), int(attacking_number[2])
#     if field[row][column] > 0:
#         field[row][column] -= 1
#         if field[row][column] == 0:
#             destroyed_ships += 1

# print(destroyed_ships)
