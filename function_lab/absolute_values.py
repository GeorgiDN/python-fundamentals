def take_input():
    return list(map(float, input().split(" ")))


def take_abs_values(values):
    return [abs(num) for num in values]


def print_result(result):
    return print(result)


current_input = take_input()
print_result(take_abs_values(current_input))




##
# def print_absolute_values():
#     return print([abs(num) for num in list(map(float, input().split(" ")))])
#
#
# print_absolute_values()




##
# print([abs(num) for num in list(map(float, input().split(" ")))])




##
# number_list = input().split()
# absolute_value = []
#
# for num in number_list:
#     absolute_value.append(abs(float(num)))
#
# print(absolute_value)
