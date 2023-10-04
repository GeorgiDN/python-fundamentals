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
