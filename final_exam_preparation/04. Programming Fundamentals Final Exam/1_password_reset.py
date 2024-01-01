password = input()

while True:
    command = input()
    if command == "Done":
        break

    parts = command.split()
    action = parts[0]

    if action == "TakeOdd":
        new_password = ""
        for idx, letter in enumerate(password):
            if idx % 2 != 0:
                new_password += letter
        password = new_password
        print(password)

    elif action == "Cut":
        cut_index, length = int(parts[1]), int(parts[2])
        password = password[:cut_index] + password[cut_index + length:]
        print(password)

    elif action == "Substitute":
        substring, substitute = parts[1], parts[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
