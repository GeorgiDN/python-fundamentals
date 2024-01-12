def maximum_multiple(div, bound):
    largest_num = 0
    for i in range(div, bound + 1):
        if i % div == 0:
            largest_num = i
    return largest_num


divisor = int(input())
boundary = int(input())
print(maximum_multiple(divisor, boundary))





# divisor = int(input())
# boundary = int(input())

# largest_num = 0

# for i in range(divisor, boundary + 1):
#     if i % divisor == 0:
#         largest_num = i

# print(largest_num)
