final_message = []

while True:
    command = input()
    if command == "end":
        break

    data = command.split()

    if data[0] == "Chat":
        chat_message = data[1]
        final_message.append(chat_message)

    elif data[0] == "Delete":
        delete_message = data[1]
        if delete_message in final_message:
            final_message.remove(delete_message)

    elif data[0] == "Edit":
        old_message, edit_message = data[1], data[2]
        if old_message in final_message:
            index_to_insert = final_message.index(old_message)
            final_message[index_to_insert] = edit_message

    elif data[0] == "Pin":
        pin_message = data[1]
        if pin_message in final_message:
            final_message.remove(pin_message)
            final_message.append(pin_message)

    elif data[0] == "Spam":
        messages = data[1:]
        for message in messages:
            final_message.append(message)

for curr_message in final_message:
    print(curr_message)
  
