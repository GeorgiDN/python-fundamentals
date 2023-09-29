operator = input()
num_1 = int(input())
num_2 = int(input())

def solve(num_1, num_2, operator):
    result = None
    if operator == 'multiply':
        result = num_1 * num_2
    elif operator == 'divide':
        result = int(num_1 / num_2)
    elif operator == 'add':
        result = num_1 + num_2
    elif operator == 'subtract':
        result = num_1 - num_2
    return result

print(solve(num_1, num_2, operator))

