list_numbers = [int(x) for x in input().split(", ")]
sorted_groups = {}
group = 0

while True:
    if len(list_numbers) == 0:
        break

    if max(list_numbers) > group:
        group += 10

    sorted_groups[group] = [num for num in list_numbers if num <= group]
    list_numbers = [x for x in list_numbers if x > group]

for key, value in sorted_groups.items():
    print(f"Group of {key}'s: {value}")



# numbers_list = list(map(int, input().split(', ')))
#
# max_value_of_group = 10
# groups = {}
#
# while numbers_list:
#     numbers_according_group = [num for num in numbers_list if max_value_of_group - 10 < num <= max_value_of_group]
#     groups[max_value_of_group] = numbers_according_group
#     numbers_list = [num for num in numbers_list if num not in numbers_according_group]
#
#     max_value_of_group += 10
#
# for group, numbers in sorted(groups.items()):
#     print(f"Group of {group}'s: {numbers}")
