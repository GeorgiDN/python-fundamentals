string = input()

my_list = string.split(' ')

my_list = [int(num) for num in my_list]

changed_result = []

for digit in my_list:
    reversed_digit = digit * (-1)
    changed_result.append(reversed_digit)

print(changed_result)
