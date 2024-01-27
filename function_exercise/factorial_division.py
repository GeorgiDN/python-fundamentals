def factorial_division(first_num, second_num):
    return round(factorial(first_num) / factorial(second_num), 2)


def factorial(num):
    factorial_result = 1
    for i in range(1, num + 1):
        factorial_result *= i
    return factorial_result


first_number = int(input())
second_number = int(input())

result = factorial_division(first_number, second_number)
print(f"{result:.2f}")
