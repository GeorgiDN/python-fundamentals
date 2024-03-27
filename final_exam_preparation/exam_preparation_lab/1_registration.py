def is_valid_index(text, idx):
    return 0 <= idx < len(text)


def change_letters(name, kind_):
    current_username = ''
    if kind_ == "Lower":
        for ch in name:
            current_username += ch.lower()
    elif kind_ == "Upper":
        for ch in name:
            current_username += ch.upper()
    print(current_username)
    return current_username


def reverse_substring(curr_username, start_idx, end_idx):
    if is_valid_index(curr_username, start_idx) and is_valid_index(curr_username, end_idx):
        curr_substring = curr_username[start_idx: end_idx + 1]
        curr_substring = curr_substring[::-1]
        return print(curr_substring)


def cut_substring(curr_username, substring_):
    if substring_ in curr_username:
        curr_username = curr_username.replace(substring_, "")
        print(curr_username)
    else:
        print(f"The username {curr_username} doesn't contain {substring_}.")
    return curr_username


def replace_char(curr_username, char):
    curr_username = curr_username.replace(char, "-")
    print(curr_username)
    return curr_username


def check_is_valid_char(curr_username, char):
    if char not in curr_username:
        return print(f"{char} must be contained in your username.")
    return print("Valid username.")


def main():
    username = input()

    while True:
        command = input()
        if command == "Registration":
            break

        data = command.split()
        command = data[0]

        if command == "Letters":
            kind = data[1]
            username = change_letters(username, kind)

        elif command == "Reverse":
            start_index, end_index = int(data[1]), int(data[2])
            reverse_substring(username, start_index, end_index)

        elif command == "Substring":
            substring = data[1]
            username = cut_substring(username, substring)

        elif command == "Replace":
            character = data[1]
            username = replace_char(username, character)

        elif command == "IsValid":
            character = data[1]
            check_is_valid_char(username, character)


if __name__ == '__main__':
    main()
    
