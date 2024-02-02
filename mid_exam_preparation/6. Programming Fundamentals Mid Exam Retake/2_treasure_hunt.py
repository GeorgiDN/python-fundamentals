def is_valid(lst, idx):
    return 0 <= idx < len(lst)


def loot(elements_list, *loot_parameters):
    for loot_elements in loot_parameters:
        for element in loot_elements:
            if element not in elements_list:
                elements_list.insert(0, element)
    return elements_list


def drop(elements_list, drop_index):
    if is_valid(elements_list, drop_index):
        if len(elements_list) - 1 > 0:
            curr_element = elements_list.pop(drop_index)
            elements_list.append(curr_element)
    return elements_list


def steal(elements_list, steal_count):
    stolen_items = []
    for _ in range(steal_count):
        if elements_list:
            if len(elements_list) - 1 > 0:
                steal_element = elements_list.pop()
            else:
                steal_element = elements_list[0]
                elements_list.remove(steal_element)
            stolen_items.append(steal_element)

    if stolen_items:
        stolen_items = stolen_items[::-1]
        print(', '.join(stolen_items))
    return elements_list


def implement_treasure_hunt(elements):
    while True:
        command = input()
        if command == "Yohoho!":
            break
        info = command.split(" ")
        current_command = info[0]

        if current_command == "Loot":
            loot_items = info[1:]
            elements = loot(elements, loot_items)

        elif current_command == "Drop":
            drop_index = int(info[1])
            elements = drop(elements, drop_index)

        elif current_command == "Steal":
            steal_count = int(info[1])
            elements = steal(elements, steal_count)

    return elements


treasure_hunt_items = input().split("|")
treasure_hunt_items = implement_treasure_hunt(treasure_hunt_items)

if treasure_hunt_items:
    chest = []
    sum_of_letters = 0
    for item in treasure_hunt_items:
        sum_of_letters += len(item)
        chest.append(item)
    average_treasure_gain = sum_of_letters / len(chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
