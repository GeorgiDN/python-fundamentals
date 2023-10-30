n = int(input())

registered = {}

for i in range(n):
    command = input().split()
    if command[0] == 'register':
        name = command[1]
        number = command[2]

        if name not in registered:
            registered[name] = number
            print(f"{name} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")

    elif command[0] == 'unregister':
        name = command[1]
        if name not in registered:
            print(f"ERROR: user {name} not found")
        else:
            registered.pop(name)
            print(f"{name} unregistered successfully")


for name, number in registered.items():
    print(f"{name} => {number}")
