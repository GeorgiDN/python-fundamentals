lines = int(input())

balance = 0

for _ in range(lines):
    expression = input()

    if expression == '(':
        balance += 1
    elif expression == ')':
        balance -= 1

    if balance < 0:
        print('UNBALANCED')
        break

if balance == 0:
    print('BALANCED')
elif balance > 0:
    print('UNBALANCED')
    
