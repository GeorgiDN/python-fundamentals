def tribonacci(n):

    a = 0
    b = 1
    c = 1

    print(b, c, end=' ')

    for i in range(2, n):
        d = a + b + c
        a = b
        b = c
        c = d
        print(d, end=' ')

num = int(input())

tribonacci(num)
