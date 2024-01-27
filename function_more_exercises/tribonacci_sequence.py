def take_tribonacci_sequence(number):
    a, b, c = 1, 1, 2
    tribonacci_list = [a]
    if number > 1:
        tribonacci_list.append(b)
    if number > 2:
        tribonacci_list.append(c)
    while len(tribonacci_list) < number:
        for _ in range(number - 3):
            current_num = a + b + c
            a = b
            b = c
            c = current_num
            tribonacci_list.append(current_num)

    return tribonacci_list


user_number = int(input())
print(*take_tribonacci_sequence(user_number))


# 90/100
# def tribonacci(n):

#     a = 0
#     b = 1
#     c = 1

#     print(b, c, end=' ')

#     for i in range(2, n):
#         d = a + b + c
#         a = b
#         b = c
#         c = d
#         print(d, end=' ')

# num = int(input())

# tribonacci(num)
