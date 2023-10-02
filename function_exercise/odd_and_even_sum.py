numbers_input = input()
number_list = [int(digit) for digit in str(numbers_input)]

def sum_all(numbers):
    even_sum = 0
    odd_sum = 0
    for num in number_list:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

sum_all(number_list)
