import math

def longest_to_center(n1, n2, n3, n4, n5, n6, n7, n8):
    result = None
    first_coordinates = abs(n1) + abs(n2) + abs(n3) + abs(n4)
    second_coordinates = abs(n5) + abs(n6) + abs(n7) + abs(n8)

    first_sum = abs(n1) + abs(n2)
    second_sum = abs(n3) + abs(n4)
    third_sum = abs(n5) + abs(n6)
    fourth_sum = abs(n7) + abs(n8)

    if first_coordinates >= second_coordinates:
        if first_sum <= second_sum:
            result = f'({math.floor(n1)}, {math.floor(n2)})({math.floor(n3)}, {math.floor(n4)})'
        elif first_sum > second_sum:
            result = f'({math.floor(n3)}, {math.floor(n4)})({math.floor(n1)}, {math.floor(n2)})'
    else:
        if third_sum <= fourth_sum:
            result = f'({math.floor(n5)}, {math.floor(n6)})({math.floor(n7)}, {math.floor(n8)})'
        elif third_sum > fourth_sum:
            result = f'({math.floor(n7)}, {math.floor(n8)})({math.floor(n5)}, {math.floor(n6)})'

    return result

num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())
num_6 = float(input())
num_7 = float(input())
num_8 = float(input())

print(longest_to_center(num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8))
