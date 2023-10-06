import math

def closest_to_center(n1, n2, n3, n4):
    first_coordinates = abs(n1) + abs(n2)
    second_coordinates = abs(n3) + abs(n4)

    if first_coordinates <= second_coordinates:
        result = f'({math.floor(n1)}, {math.floor(n2)})'
    else:
        result = f'({math.floor(n3)}, {math.floor(n4)})'

    return result

num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())

print(closest_to_center(num_1, num_2, num_3, num_4))
