def sum_numbers(a, b):
    return a + b

def subtract(a, b, c):
    return sum_numbers(a, b) - c

def add_and_subtract():
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    result = subtract(num_1, num_2, num_3)
    print(result)

add_and_subtract()
