import math


def closest_to_the_center_point(x1, y1, x2, y2):
    first_sum = abs(x1) + abs(y1)
    second_sum = abs(x2) + abs(y2)

    if first_sum <= second_sum:
        return f"({math.floor(x1)}, {math.floor(y1)})"
    return f"({math.floor(x2)}, {math.floor(y2)})"


X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())

print(closest_to_the_center_point(X1, Y1, X2, Y2))


# import math

# def closest_to_center(n1, n2, n3, n4):
#     first_coordinates = abs(n1) + abs(n2)
#     second_coordinates = abs(n3) + abs(n4)

#     if first_coordinates <= second_coordinates:
#         result = f'({math.floor(n1)}, {math.floor(n2)})'
#     else:
#         result = f'({math.floor(n3)}, {math.floor(n4)})'

#     return result

# num_1 = float(input())
# num_2 = float(input())
# num_3 = float(input())
# num_4 = float(input())

# print(closest_to_center(num_1, num_2, num_3, num_4))
