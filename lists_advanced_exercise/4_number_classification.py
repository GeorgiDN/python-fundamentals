def fill_list_with_numbers():
    return [int(x) for x in input().split(", ")]


def get_positives(numbers):
    return [num for num in numbers if num >= 0]


def get_negatives(numbers):
    return [num for num in numbers if num < 0]


def get_evens(numbers):
    return [num for num in numbers if num % 2 == 0]


def get_odds(numbers):
    return [num for num in numbers if num % 2 != 0]


def print_result(positive, negative, even, odd):
    return print(f"Positive: {', '.join(map(str, positive))}\n"
                 f"Negative: {', '.join(map(str, negative))}\n"
                 f"Even: {', '.join(map(str, even))}\n"
                 f"Odd: {', '.join(map(str, odd))}")


list_with_numbers = fill_list_with_numbers()
positives = get_positives(list_with_numbers)
negatives = get_negatives(list_with_numbers)
evens = get_evens(list_with_numbers)
odds = get_odds(list_with_numbers)
print_result(positives, negatives, evens, odds)




# list_with_numbers = [int(x) for x in input().split(", ")]
# 
# positives = [num for num in list_with_numbers if num >= 0]
# negatives = [num for num in list_with_numbers if num < 0]
# evens = [num for num in list_with_numbers if num % 2 == 0]
# odds = [num for num in list_with_numbers if num % 2 != 0]
# 
# print(f"Positive: {', '.join(map(str, positives))}\n"
#       f"Negative: {', '.join(map(str, negatives))}\n"
#       f"Even: {', '.join(map(str, evens))}\n"
#       f"Odd: {', '.join(map(str, odds))}")




# numbers = list(map(int, input().split(', ')))

# positive_numbers = filter(lambda x: x >= 0, numbers)
# negative_numbers = filter(lambda y: y < 0, numbers)
# even_numbers = filter(lambda z: z % 2 == 0, numbers)
# odd_numbers = filter(lambda a: a % 2 != 0, numbers)

# positive_numbers_list = ', '.join([str(positive) for positive in positive_numbers])
# negative_numbers_list = ', '.join([str(negative) for negative in negative_numbers])
# even_numbers_list = ', '.join([str(even) for even in even_numbers])
# odd_numbers_list = ', '.join([str(odd) for odd in odd_numbers])

# print(f"Positive: {positive_numbers_list}")
# print(f'Negative: {negative_numbers_list}')
# print(f'Even: {even_numbers_list}')
# print(f'Odd: {odd_numbers_list}')
