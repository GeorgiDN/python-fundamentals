def collect(list_items, col_item):
    if col_item not in list_items:
        list_items.append(col_item)
    return list_items


def drop(list_items, dr_item):
    if dr_item in list_items:
        list_items.remove(dr_item)
    return list_items


def combine_items(list_items, old_item_, new_item_):
    if old_item_ in list_items:
        index_old_item = list_items.index(old_item_)
        if index_old_item + 1 < len(list_items):
            list_items.insert(index_old_item + 1, new_item_)
        else:
            list_items.append(new_item_)
    return list_items

def renew(list_items, ren_item):
    if ren_item in list_items:
        list_items.remove(ren_item)
        list_items.append(ren_item)
    return list_items


def inventory():
    items_list = input().split(", ")
    while True:
        command = input()
        if command == "Craft!":
            break

        data = command.split(" - ")
        if data[0] == "Collect":
            collect_item = data[1]
            items_list = collect(items_list, collect_item)

        elif data[0] == "Drop":
            drop_item = data[1]
            items_list = drop(items_list, drop_item)

        elif data[0] == "Combine Items":
            two_items = data[1]
            old_item, new_item = two_items.split(":")
            items_list = combine_items(items_list, old_item, new_item)

        elif data[0] == "Renew":
            renew_item = data[1]
            items_list = renew(items_list, renew_item)

    print(", ".join(items_list))


inventory()
