n = int(input())

if n < 2:
    print('False')
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print('True')
    else:
        print('False')
      
