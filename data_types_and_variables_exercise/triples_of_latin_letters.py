number_of_symbols = int(input())
field = [[[f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}\n' for k in range(number_of_symbols)] for j in range(number_of_symbols)] for i in range(number_of_symbols)]

result = "".join("".join("".join(matrix) for matrix in row) for row in field)
print(result)



# num = int(input())

# for i in range(num):
#     for j in range(num):
#         for k in range(num):
#             print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')
