def register(park_slots, username, lic_number):
    if username in park_slots:
        print(f"ERROR: already registered with plate number {lic_number}")
    else:
        park_slots[username] = lic_number
        print(f"{username} registered {lic_number} successfully")
    return park_slots


def unregister(park_slots, username):
    if username not in park_slots:
        print(f"ERROR: user {username} not found")
    else:
        del park_slots[username]
        print(f"{username} unregistered successfully")
    return park_slots


def print_result(park_slots):
    print('\n'.join([f"{name_} => {num}" for name_, num in park_slots.items()]))


def softuni_parking():
    parking_slots = {}
    number_of_commands = int(input())

    for _ in range(number_of_commands):
        data = input()
        info = data.split(" ")
        command = info[0]
        if command == "register":
            name, license_number = info[1], info[2]
            parking_slots = register(parking_slots, name, license_number)

        elif command == "unregister":
            name = info[1]
            parking_slots = unregister(parking_slots, name)

    print_result(parking_slots)


softuni_parking()





# n = int(input())

# registered = {}

# for i in range(n):
#     command = input().split()
#     if command[0] == 'register':
#         name = command[1]
#         number = command[2]

#         if name not in registered:
#             registered[name] = number
#             print(f"{name} registered {number} successfully")
#         else:
#             print(f"ERROR: already registered with plate number {number}")

#     elif command[0] == 'unregister':
#         name = command[1]
#         if name not in registered:
#             print(f"ERROR: user {name} not found")
#         else:
#             registered.pop(name)
#             print(f"{name} unregistered successfully")


# for name, number in registered.items():
#     print(f"{name} => {number}")
