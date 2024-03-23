def take_odd(text):
    new_text = ''
    for i, letter in enumerate(text):
        if i % 2 != 0:
            new_text += letter
    print(new_text)
    return new_text


def cut_text(text, idx, length_):
    substring = text[idx: idx + length_]
    text = text.replace(substring, '', 1)
    print(text)
    return text


def substitute_text(text, substring_, substitute_):
    if substring_ in text:
        text = text.replace(substring_, substitute_)
        print(text)
    else:
        print("Nothing to replace!")
    return text


def main():
    password = input()
    while True:
        command = input()
        if command == "Done":
            break
        data = command.split()
        command = data[0]
        if command == "TakeOdd":
            password = take_odd(password)

        elif command == "Cut":
            index, length = int(data[1]), int(data[2])
            password = cut_text(password, index, length)

        elif command == "Substitute":
            substring, substitute = data[1], data[2]
            password = substitute_text(password, substring, substitute)

    print(f"Your password is: {password}")


if __name__ == '__main__':
    main()






# password = input()

# while True:
#     command = input()
#     if command == "Done":
#         break

#     parts = command.split()
#     action = parts[0]

#     if action == "TakeOdd":
#         new_password = ""
#         for idx, letter in enumerate(password):
#             if idx % 2 != 0:
#                 new_password += letter
#         password = new_password
#         print(password)

#     elif action == "Cut":
#         cut_index, length = int(parts[1]), int(parts[2])
#         password = password[:cut_index] + password[cut_index + length:]
#         print(password)

#     elif action == "Substitute":
#         substring, substitute = parts[1], parts[2]
#         if substring in password:
#             password = password.replace(substring, substitute)
#             print(password)
#         else:
#             print("Nothing to replace!")

# print(f"Your password is: {password}")

