def urgent(ur_it, sh_l):
    if ur_it not in sh_l:
        sh_l.insert(0, ur_it)
    return sh_l


def unnecessary(unnec_it, sh_l):
    if unnec_it in sh_l:
        sh_l.remove(unnec_it)
    return sh_l


def correct(old_it, new_it, sh_l):
    if old_it in sh_l:
        idx_replace = sh_l.index(old_it)
        sh_l[idx_replace] = new_it
    return sh_l


def rearrange(item_, sh_l):
    if item_ in sh_l:
        idx_item_ = sh_l.index(item_)
        rearange_item = sh_l.pop(idx_item_)
        sh_l.append(rearange_item)
    return sh_l


def main():
    shopping_list = input().split('!')

    while True:
        command = input()
        if command == "Go Shopping!":
            break

        info = command.split(" ")
        if info[0] == "Urgent":
            urgent_item = info[1]
            urgent(urgent_item, shopping_list)

        elif info[0] == "Unnecessary":
            unnecessary_item = info[1]
            unnecessary(unnecessary_item, shopping_list)

        elif info[0] == "Correct":
            old_item, new_item = info[1], info[2]
            correct(old_item, new_item, shopping_list)

        elif info[0] == "Rearrange":
            item = info[1]
            rearrange(item, shopping_list)

    print(', '.join(shopping_list))


if __name__ == "__main__":
    main()
