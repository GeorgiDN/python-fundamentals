text = input()

while True:
    command = input()
    if command == "Done":
        break
    data = command.split()
    command = data[0]

    if command == "Change":
        character = data[1]
        replacement = data[2]
        text = text.replace(character, replacement)
        print(text)

    elif command == "Includes":
        word = data[1]
        print("True") if word in text else print("False")

    elif command == "End":
        word = data[1]
        print("True") if text.endswith(word) else print("False")

    elif command == "Uppercase":
        text = text.upper()
        print(text)

    elif command == "FindIndex":
        symbol = data[1]
        index = text.find(symbol)
        print(index)

    elif command == "Cut":
        start_index = int(data[1])
        count = int(data[2])
        text = text[start_index:start_index + count]
        print(text)
