n = int(input())

list_even = []
list_odd = []
list_negative = []
list_positive = []

for _ in range(n):
    command = int(input())
    if command % 2 == 0 or command == 0:
        list_even.append(command)
        if command >= 0:
            list_positive.append(command)
        else:
            list_negative.append(command)
    else:
        list_odd.append(command)
        if command >= 0:
            list_positive.append(command)
        else:
            list_negative.append(command)

command = input()
if command == 'even':
    print(list_even)
elif command == 'odd':
    print(list_odd)
elif command == 'positive':
    print(list_positive)
elif command == 'negative':
    print(list_negative)
  
