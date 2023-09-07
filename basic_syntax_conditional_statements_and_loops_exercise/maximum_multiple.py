divisor = int(input())
boundary = int(input())

largest_num = 0

for i in range(divisor, boundary + 1):
    if i % divisor == 0:
        largest_num = i

print(largest_num)
