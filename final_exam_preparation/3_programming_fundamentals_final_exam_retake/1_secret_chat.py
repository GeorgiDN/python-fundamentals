text = input()

while True:
    command = input()
    if command == "Reveal":
        break

    parts = command.split(":|:")
    action = parts[0]

    if action == "InsertSpace":
        idx = int(parts[1])
        text = text[:idx] + ' ' + text[idx:]
        print(text)

    elif action == "Reverse":
        substring = parts[1]
        if substring in text:
            text = text.replace(substring, '', 1)
            text = text + substring[::-1]
            print(text)
        else:
            print("error")

    elif action == "ChangeAll":
        substring_for_change = parts[1]
        replacement = parts[2]
        if substring_for_change in text:
            while substring_for_change in text:
                text = text.replace(substring_for_change, replacement)
        print(text)

print(f"You have a new text message: {text}")
