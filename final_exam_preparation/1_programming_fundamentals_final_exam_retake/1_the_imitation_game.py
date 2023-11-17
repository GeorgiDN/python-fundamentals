text = input()
while True:
    command = input()
    if command == "Decode":
        break

    parts = command.split("|")
    action = parts[0]

    if action == 'Move':
        num_of_letters = int(parts[1])
        if num_of_letters <= len(text):
            text = text[num_of_letters:] + text[:num_of_letters]

    elif action == 'Insert':
        index = int(parts[1])
        value = parts[2]

        part1 = text[:index]
        part2 = text[index:]
        text = part1 + value + part2

    elif action == 'ChangeAll':
        substring = parts[1]
        replacement = parts[2]
        text = text.replace(substring, replacement)

print(f"The decrypted message is: {text}")
