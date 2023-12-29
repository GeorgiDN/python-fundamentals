shopping_list = input().split('!')

while True:
    command = input()
    if command == "Go Shopping!":
        break

    info = command.split(" ")

    if info[0] == "Urgent":
        urgent_item = info[1]
        if urgent_item not in shopping_list:
            shopping_list.insert(0, urgent_item)

    elif info[0] == "Unnecessary":
        unnecessary_item = info[1]
        if unnecessary_item in shopping_list:
            shopping_list.remove(unnecessary_item)

    elif info[0] == "Correct":
        old_item, new_item = info[1], info[2]
        if old_item in shopping_list:
            idx_for_replace = shopping_list.index(old_item)
            shopping_list[idx_for_replace] = new_item

    elif info[0] == "Rearrange":
        item = info[1]
        if item in shopping_list:
            idx_item = shopping_list.index(item)
            rearrange_item = shopping_list.pop(idx_item)
            shopping_list.append(rearrange_item)

print(', '.join(shopping_list))
