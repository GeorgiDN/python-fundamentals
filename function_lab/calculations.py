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


current_operator = input()
number_1 = int(input())
number_2 = int(input())
print(solve(number_1, number_2, current_operator))

