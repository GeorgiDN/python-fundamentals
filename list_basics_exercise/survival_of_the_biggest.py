list_with_numbers = [int(x) for x in input().split(" ")]
number_for_remove = int(input())

for _ in range(number_for_remove):
    index_min_number = list_with_numbers.index(min(list_with_numbers))
    list_with_numbers.pop(index_min_number)

print(', '.join(map(str, list_with_numbers)))


# list_of_numbers = input().split()
# n = int(input())

# list_numbers = [int(num) for num in list_of_numbers]

# for i in range(n):
#     min_value = min(list_numbers)
#     list_numbers.remove(min_value)

# print(", ".join(map(str, list_numbers)))
