name = input()
char = 0

while name != 'Welcome!':
    if name == 'Voldemort':
        print('You must not speak of that name!')
        break
    for i in name:
        char += 1
    if char < 5:
        print(f"{name} goes to Gryffindor.")
    elif char == 5:
        print(f"{name} goes to Slytherin.")
    elif char == 6:
        print(f"{name} goes to Ravenclaw.")
    elif char > 6:
        print(f"{name} goes to Hufflepuff.")

    char = 0
    name = input()

if name == 'Welcome!':
    print('Welcome to Hogwarts.')
