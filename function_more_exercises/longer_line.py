import math


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_sum = abs(x1) + abs(y1)
    second_sum = abs(x2) + abs(y2)

    third_sum = abs(x3) + abs(y3)
    fourth_sum = abs(x4) + abs(y4)

    first_coordinates = first_sum + second_sum
    second_coordinates = third_sum + fourth_sum

    if first_coordinates >= second_coordinates:
        if first_sum <= second_sum:
            return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"
        else:
            return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"
    else:
        if third_sum <= fourth_sum:
            return f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})"
        else:
            return f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})"


X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())
X3 = float(input())
Y3 = float(input())
X4 = float(input())
Y4 = float(input())

print(longer_line(X1, Y1, X2, Y2, X3, Y3, X4, Y4))



# import math

# def longest_to_center(n1, n2, n3, n4, n5, n6, n7, n8):
#     result = None
#     first_coordinates = abs(n1) + abs(n2) + abs(n3) + abs(n4)
#     second_coordinates = abs(n5) + abs(n6) + abs(n7) + abs(n8)

#     first_sum = abs(n1) + abs(n2)
#     second_sum = abs(n3) + abs(n4)
#     third_sum = abs(n5) + abs(n6)
#     fourth_sum = abs(n7) + abs(n8)

#     if first_coordinates >= second_coordinates:
#         if first_sum <= second_sum:
#             result = f'({math.floor(n1)}, {math.floor(n2)})({math.floor(n3)}, {math.floor(n4)})'
#         elif first_sum > second_sum:
#             result = f'({math.floor(n3)}, {math.floor(n4)})({math.floor(n1)}, {math.floor(n2)})'
#     else:
#         if third_sum <= fourth_sum:
#             result = f'({math.floor(n5)}, {math.floor(n6)})({math.floor(n7)}, {math.floor(n8)})'
#         elif third_sum > fourth_sum:
#             result = f'({math.floor(n7)}, {math.floor(n8)})({math.floor(n5)}, {math.floor(n6)})'

#     return result

# num_1 = float(input())
# num_2 = float(input())
# num_3 = float(input())
# num_4 = float(input())
# num_5 = float(input())
# num_6 = float(input())
# num_7 = float(input())
# num_8 = float(input())

# print(longest_to_center(num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8))
