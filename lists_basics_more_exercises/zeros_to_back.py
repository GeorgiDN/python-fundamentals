string = input()
my_list = list(map(int, string.split(', ')))

zeros = []
non_zeros = []

for num in my_list:
    if num == 0:
        zeros.append(num)
    else:
        non_zeros.append(num)

result = non_zeros + zeros
print(result)



# advanced
# input_string = input()
# numbers = [int(x) for x in input_string.split(", ")]

# zeros = numbers.count(0)  # Count the number of zeros in the list
# non_zeros = [num for num in numbers if num != 0]  # Create a list of non-zero numbers

# result = non_zeros + [0] * zeros  # Concatenate the non-zero list with zeros

# print(result)
