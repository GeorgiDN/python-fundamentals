numbers = list(map(int, input().split(', ')))

positive_numbers = filter(lambda x: x >= 0, numbers)
negative_numbers = filter(lambda y: y < 0, numbers)
even_numbers = filter(lambda z: z % 2 == 0, numbers)
odd_numbers = filter(lambda a: a % 2 != 0, numbers)

positive_numbers_list = ', '.join([str(positive) for positive in positive_numbers])
negative_numbers_list = ', '.join([str(negative) for negative in negative_numbers])
even_numbers_list = ', '.join([str(even) for even in even_numbers])
odd_numbers_list = ', '.join([str(odd) for odd in odd_numbers])

print(f"Positive: {positive_numbers_list}")
print(f'Negative: {negative_numbers_list}')
print(f'Even: {even_numbers_list}')
print(f'Odd: {odd_numbers_list}')
