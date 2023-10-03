number_list = list(map(int, input().split()))

def min_max_sum():
    min_number = min(number_list)
    max_number = max(number_list)
    sum_number = sum(number_list)

    print(f"The minimum number is {min_number}\n"
          f"The maximum number is {max_number}\n"
          f"The sum number is: {sum_number}")

min_max_sum()
