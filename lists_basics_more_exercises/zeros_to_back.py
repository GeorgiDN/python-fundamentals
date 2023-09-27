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
