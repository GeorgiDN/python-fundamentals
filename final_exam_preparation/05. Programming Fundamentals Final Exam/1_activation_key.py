def contains(text, substring_):
    if substring_ in text:
        print(f"{text} contains {substring_}")
    else:
        print("Substring not found!")


def flip_upper(text, start_idx, end_idx):
    text = text[:start_idx] + text[start_idx:end_idx].upper() + text[end_idx:]
    print(text)
    return text


def flip_lower(text, start_idx, end_idx):
    text = text[:start_idx] + text[start_idx:end_idx].lower() + text[end_idx:]
    print(text)
    return text


def slice_(text, start_idx, end_idx):
    text = text[:start_idx] + text[end_idx:]
    print(text)
    return text


def main():
    activation_key = input()
    while True:
        command = input()
        if command == "Generate":
            break

        info = command.split(">>>")
        command = info[0]

        if command == "Contains":
            substring = info[1]
            contains(activation_key, substring)

        elif command == "Flip":
            kind = info[1]
            start_index, end_index = int(info[2]), int(info[3])
            if kind == "Upper":
                activation_key = flip_upper(activation_key, start_index, end_index)

            elif kind == "Lower":
                activation_key = flip_lower(activation_key, start_index, end_index)

        elif command == "Slice":
            start_index, end_index = int(info[1]), int(info[2])
            activation_key = slice_(activation_key, start_index, end_index)

    print(f"Your activation key is: {activation_key}")


if __name__ == "__main__":
    main()
