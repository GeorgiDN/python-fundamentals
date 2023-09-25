gifts = input().split()

command = input()

while command != "No Money":
    command_parts = command.split()
    command_type = command_parts[0]

    if command_type == "OutOfStock":
        gift = command_parts[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"

    elif command_type == "Required":
        gift = command_parts[1]
        index = int(command_parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif command_type == "JustInCase":
        gift = command_parts[1]
        gifts[-1] = gift

    command = input()

final_gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(final_gifts))
