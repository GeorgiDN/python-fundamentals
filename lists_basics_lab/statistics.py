def take_int_input():
      return int(input())


def take_numbers(lines):
      numbers = [take_int_input() for _ in range(lines)]
      return numbers


def find_positive_numbers(nums):
      positive_list = [num for num in nums if num >= 0]
      return positive_list


def find_negative_numbers(nums):
      negative_list = [num for num in nums if num < 0]
      return negative_list


def counts_of_positives(lst):
      return len(lst)


def sum_negatives(lst):
      return sum(lst)


def print_result(pos_list, neg_list):
      result = ""
      result += f'{pos_list}\n' \
                f'{neg_list}\n' \
                f'Count of positives: {counts_of_positives(pos_list)}\n' \
                f'Sum of negatives: {sum_negatives(neg_list)}'

      return print(result)


rows = take_int_input()
numbers = take_numbers(rows)
my_positive_list = find_positive_numbers(numbers)
my_negative_list = find_negative_numbers(numbers)
print_result(my_positive_list, my_negative_list)




##
# lines = int(input())

# numbers = [int(input()) for _ in range(lines)]
# my_positive_list = [num for num in numbers if num >= 0]
# my_negative_list = [num for num in numbers if num < 0]

# print(f'{my_positive_list}\n'
#       f'{my_negative_list}')
# print(f"Count of positives: {len(my_positive_list)}\n"
#       f"Sum of negatives: {sum(my_negative_list)}")




##
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
