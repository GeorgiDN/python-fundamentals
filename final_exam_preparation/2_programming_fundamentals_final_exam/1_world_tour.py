stops = input()

while True:
    command = input()
    if command == "Travel":
        break

    parts = command.split(":")
    action = parts[0]

    if action == "Add Stop":
        index = int(parts[1])
        string = parts[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]

    elif action == "Remove Stop":
        start_index = int(parts[1])
        end_index = int(parts[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]

    elif action == "Switch":
        old_string = parts[1]
        new_string = parts[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")

