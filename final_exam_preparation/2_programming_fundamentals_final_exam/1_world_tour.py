def is_valid_index(idx, text_):
    return 0 <= idx < len(text_)


def add_stop(text_, idx, curr_string):
    if is_valid_index(idx, text_):
        text_ = text_[:idx] + curr_string + text_[idx:]
    print(text_)
    return text_


def remove_stop(text_, start_idx, end_idx):
    if is_valid_index(start_idx, text_) and is_valid_index(end_idx, text_):
        text_ = text_[:start_idx] + text_[end_idx + 1:]
    print(text_)
    return text_


def switch(text_, old_str, new_str):
    if old_str in text_:
        text_ = text_.replace(old_str, new_str)
    print(text_)
    return text_


def main():
    text = input()
    while True:
        command = input()
        if command == 'Travel':
            break

        data = command.split(":")
        action = data[0]

        if action == "Add Stop":
            index, current_string = int(data[1]), data[2]
            text = add_stop(text, index, current_string)

        elif action == "Remove Stop":
            start_index, end_index = int(data[1]), int(data[2])
            text = remove_stop(text, start_index, end_index)

        elif action == "Switch":
            old_string, new_string = data[1], data[2]
            text = switch(text, old_string, new_string)

    print(f"Ready for world tour! Planned stops: {text}")


if __name__ == "__main__":
    main()




# stops = input()

# while True:
#     command = input()
#     if command == "Travel":
#         break

#     parts = command.split(":")
#     action = parts[0]

#     if action == "Add Stop":
#         index = int(parts[1])
#         string = parts[2]
#         if 0 <= index < len(stops):
#             stops = stops[:index] + string + stops[index:]

#     elif action == "Remove Stop":
#         start_index = int(parts[1])
#         end_index = int(parts[2])
#         if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
#             stops = stops[:start_index] + stops[end_index + 1:]

#     elif action == "Switch":
#         old_string = parts[1]
#         new_string = parts[2]
#         if old_string in stops:
#             stops = stops.replace(old_string, new_string)

#     print(stops)

# print(f"Ready for world tour! Planned stops: {stops}")

