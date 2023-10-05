def factorial(num):
    sum_of_multiplies = 1
    if num > 0:
        for i in range(1, num + 1):
            sum_of_multiplies *= i
    return sum_of_multiplies

number = int(input())
number_2 = int(input())

result = factorial(number) / number_2
print(f'{result:.2f}')




# def factoriall(n):

#     factoriall = 1

#     for i in range(n):
#         factoriall *= i + 1

#     return factoriall

# num_1 = int(input())
# num_2 = int(input())

# result = factoriall(num_1) / num_2
# print(f'{result:.2f}')
