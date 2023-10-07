def multiplication_sign(n1, n2, n3):
    result = n1 * n2 * n3
    if result > 0:
        print('positive')
    elif result == 0:
        print('zero')
    else:
        print('negative')

num1 = int(input())
num2 = int(input())
num3 = int(input())

multiplication_sign(num1, num2, num3)



# def multiplication_sign(n1, n2, n3):
#     positive_count = 0
#     negative_count = 0
#     zero_condition = False

#     if n1 > 0:
#         positive_count += 1
#     elif n1 < 0:
#         negative_count += 1
#     else:
#         zero_condition = True
#     if n2 > 0:
#         positive_count += 1
#     elif n2 < 0:
#         negative_count += 1
#     else:
#         zero_condition = True
#     if n3 > 0:
#         positive_count += 1
#     elif n3 < 0:
#         negative_count += 1
#     else:
#         zero_condition = True

#     if not zero_condition:
#         if negative_count % 2 == 0:
#             print('positive')
#         elif negative_count % 2 != 0:
#             print('negative')
#     else:
#         print('zero')


# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# multiplication_sign(num1, num2, num3)
