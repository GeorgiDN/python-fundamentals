lines = int(input())

numbers = [int(input()) for _ in range(lines)]
my_positive_list = [num for num in numbers if num >= 0]
my_negative_list = [num for num in numbers if num < 0]

print(f'{my_positive_list}\n'
      f'{my_negative_list}')
print(f"Count of positives: {len(my_positive_list)}\n"
      f"Sum of negatives: {sum(my_negative_list)}")

# lines = int(input())

# my_positive_list = []
# my_negative_list = []

# for i in range(lines):
#     number = int(input())
#     if number >= 0:
#         my_positive_list.append(number)
#     else:
#         my_negative_list.append(number)

# length_positive_list = len(my_positive_list)
# length_negative_list = sum(my_negative_list)

# print(f'{my_positive_list}\n'
#       f'{my_negative_list}')
# print(f"Count of positives: {length_positive_list}\n"
#       f"Sum of negatives: {length_negative_list}")
