message = input()

while True:
    data = input().split('|')
    if data[0] == "Decode":
        break

    command = data[0]

    if command == "Move":
        idx = int(data[1])
        message = message[idx:] + message[:idx]

    elif command == "Insert":
        index, value = int(data[1]), data[2]
        message = message[:index] + value + message[index:]

    elif command == "ChangeAll":
        substring, replacement = data[1], data[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")




# text = input()
# while True:
#     command = input()
#     if command == "Decode":
#         break

#     parts = command.split("|")
#     action = parts[0]

#     if action == 'Move':
#         num_of_letters = int(parts[1])
#         if num_of_letters <= len(text):
#             text = text[num_of_letters:] + text[:num_of_letters]

#     elif action == 'Insert':
#         index = int(parts[1])
#         value = parts[2]

#         part1 = text[:index]
#         part2 = text[index:]
#         text = part1 + value + part2

#     elif action == 'ChangeAll':
#         substring = parts[1]
#         replacement = parts[2]
#         text = text.replace(substring, replacement)

# print(f"The decrypted message is: {text}")
