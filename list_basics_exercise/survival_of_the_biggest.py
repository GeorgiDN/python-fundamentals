list_of_numbers = input().split()
n = int(input())

list_numbers = [int(num) for num in list_of_numbers]

for i in range(n):
    min_value = min(list_numbers)
    list_numbers.remove(min_value)

print(", ".join(map(str, list_numbers)))
