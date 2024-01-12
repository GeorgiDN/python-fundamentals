def take_input():
    return input()


def sorting_hat():
    while True:
        name = take_input()
        if name == "Welcome!":
            return print("Welcome to Hogwarts.")
        if name == "Voldemort":
            return print("You must not speak of that name!")
        elif len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        elif len(name) > 6:
            print(f"{name} goes to Hufflepuff.")


sorting_hat()

# name = input()
# char = 0

# while name != 'Welcome!':
#     if name == 'Voldemort':
#         print('You must not speak of that name!')
#         break
#     for i in name:
#         char += 1
#     if char < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif char == 5:
#         print(f"{name} goes to Slytherin.")
#     elif char == 6:
#         print(f"{name} goes to Ravenclaw.")
#     elif char > 6:
#         print(f"{name} goes to Hufflepuff.")

#     char = 0
#     name = input()

# if name == 'Welcome!':
#     print('Welcome to Hogwarts.')
