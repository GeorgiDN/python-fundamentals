def list_even(list_with_numbers):
    even_list = [num for num in list_with_numbers if num % 2 == 0]

    # for num in list_with_numbers:
    #     if num % 2 == 0:
    #         even_list.append(num)
    return print(even_list)


number_list = list(map(int, input().split()))
list_even(number_list)
