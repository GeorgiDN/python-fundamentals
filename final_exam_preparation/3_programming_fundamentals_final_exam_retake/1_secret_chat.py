def insert_space(text, index):
    text = text[:index] + " " + text[index:]
    print(text)
    return text


def reverse(text, substring):
    if substring in text:
        text = text.replace(substring, '', 1)
        reversed_substring = substring[::-1]
        text = text + reversed_substring
        print(text)
    else:
        print("error")
    return text


def change_all(text, substring, replacement):
    text = text.replace(substring, replacement)
    print(text)
    return text


def main():
    text = input()

    while True:
        command = input()
        if command == "Reveal":
            break

        data = command.split(":|:")
        current_command = data[0]

        if current_command == "InsertSpace":
            index = int(data[1])
            text = insert_space(text, index)

        elif current_command == "Reverse":
            substring = data[1]
            text = reverse(text, substring)

        elif current_command == "ChangeAll":
            substring, replacement = data[1], data[2]
            text = change_all(text, substring, replacement)

    print(f"You have a new text message: {text}")


if __name__ == "__main__":
    main()




# text = input()

# while True:
#     command = input()
#     if command == "Reveal":
#         break

#     parts = command.split(":|:")
#     action = parts[0]

#     if action == "InsertSpace":
#         idx = int(parts[1])
#         text = text[:idx] + ' ' + text[idx:]
#         print(text)

#     elif action == "Reverse":
#         substring = parts[1]
#         if substring in text:
#             text = text.replace(substring, '', 1)
#             text = text + substring[::-1]
#             print(text)
#         else:
#             print("error")

#     elif action == "ChangeAll":
#         substring_for_change = parts[1]
#         replacement = parts[2]
#         if substring_for_change in text:
#             while substring_for_change in text:
#                 text = text.replace(substring_for_change, replacement)
#         print(text)

# print(f"You have a new text message: {text}")
