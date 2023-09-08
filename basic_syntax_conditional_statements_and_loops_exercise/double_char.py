command = input()

while command != 'End':
    if command == 'SoftUni':
        command = input()

    for i in command:
        print(i * 2, end='')
    print()
    command = input()
