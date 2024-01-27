number_list = list(map(int, input().split()))
even_list = list(filter(lambda num: num % 2 == 0, number_list))
print(even_list)


##
# def list_even(list_with_numbers):
#     even_list = [num for num in list_with_numbers if num % 2 == 0]

#     # for num in list_with_numbers:
#     #     if num % 2 == 0:
#     #         even_list.append(num)
#     return print(even_list)

##
# number_list = list(map(int, input().split()))
# list_even(number_list)


##
# number_list = [int(x) for x in input().split()]
# even_list = [num for num in number_list if num % 2 == 0]
# print(even_list)


##
# number_list = [int(x) for x in input().split()]
# print([num for num in number_list if num % 2 == 0])
