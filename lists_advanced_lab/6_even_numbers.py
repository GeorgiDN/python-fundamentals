number_list = list(map(int, input().split(', ')))

even_indices = []

for index, num in enumerate(number_list):
    if num % 2 == 0:
        even_indices.append(index)

print(even_indices)
