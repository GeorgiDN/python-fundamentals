def multiplication_sign(n1, n2, n3):
    result = n1 * n2 * n3
    if result > 0:
        print('positive')
    elif result == 0:
        print('zero')
    else:
        print('negative')

num1 = int(input())
num2 = int(input())
num3 = int(input())

multiplication_sign(num1, num2, num3)
