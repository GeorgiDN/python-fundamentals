def sort(list_with_numbers):
    sorted_list = list(sorted(list_with_numbers))
    print(sorted_list)


number_list = list(map(int, input().split()))
sort(number_list)


# number_list = list(map(int, input().split()))
#
# sorted_list = list(sorted(number_list))
#
# print(sorted_list)
