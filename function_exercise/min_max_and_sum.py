def min_max_sum(number_list):
    min_number = min(number_list)
    max_number = max(number_list)
    sum_number = sum(number_list)

    print(f"The minimum number is {min_number}\n"
          f"The maximum number is {max_number}\n"
          f"The sum number is: {sum_number}")


list_with_numbers = list(map(int, input().split()))
min_max_sum(list_with_numbers)
