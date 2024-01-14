def take_string_input():
    return input()


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


def find_even_numbers(nums):
      even_list = [num for num in nums if num % 2 == 0 or num == 0]
      return even_list


def find_odd_numbers(nums):
      odd_list = [num for num in nums if num % 2 != 0]
      return odd_list


def print_result(result):
    return print(result)


count_of_numbers = take_int_input()
numbers = take_numbers(count_of_numbers)
command = take_string_input()

if command == "even":
    list_evens = find_even_numbers(numbers)
    print_result(list_evens)

elif command == "odd":
    list_odds = find_odd_numbers(numbers)
    print_result(list_odds)

elif command == "negative":
    list_negatives = find_negative_numbers(numbers)
    print_result(list_negatives)

elif command == "positive":
    list_positives = find_positive_numbers(numbers)
    print_result(list_positives)




##
# n = int(input())

# list_even = []
# list_odd = []
# list_negative = []
# list_positive = []

# for _ in range(n):
#     number = int(input())
#     if number % 2 == 0 or number == 0:
#         list_even.append(number)
#         if number >= 0:
#             list_positive.append(number)
#         else:
#             list_negative.append(number)
#     else:
#         list_odd.append(number)
#         if number >= 0:
#             list_positive.append(number)
#         else:
#             list_negative.append(number)

# command = input()
# if command == 'even':
#     print(list_even)
# elif command == 'odd':
#     print(list_odd)
# elif command == 'positive':
#     print(list_positive)
# elif command == 'negative':
#     print(list_negative)
