def is_valid(lst, idx):
    return 0 <= idx < len(lst)


def take_input():
    return input()


def take_gifts():
    return [x for x in take_input().split(" ")]


def out_of_stock(lst, gift):
    for i, g in enumerate(lst):
        if g == gift:
            lst[i] = "None"
    return lst


def required_gift(lst, gift, idx):
    if is_valid(lst, idx):
        for i, g in enumerate(lst):
            if i == idx:
                lst[i] = gift
    return lst


def just_in_case(lst, gift):
    lst[-1] = gift
    return lst


def print_result(lst):
    return print(*[g for g in lst if g != "None"])


def implement_easter_gift(gifts):
    while True:
        command = take_input()
        if command == "No Money":
            break

        info = command.split(" ")
        if info[0] == "OutOfStock":
            current_gift = info[1]
            gifts = out_of_stock(gifts, current_gift)

        elif info[0] == "Required":
            req_gift, index_ = info[1], int(info[2])
            gifts = required_gift(gifts, req_gift,index_)

        elif info[0] == "JustInCase":
            just_in_case_gift = info[1]
            gifts = just_in_case(gifts, just_in_case_gift)

    return gifts


gifts_collection = take_gifts()
implement_easter_gift(gifts_collection)
print_result(gifts_collection)





# gifts = input().split()

# command = input()

# while command != "No Money":
#     command_parts = command.split()
#     command_type = command_parts[0]

#     if command_type == "OutOfStock":
#         gift = command_parts[1]
#         for i in range(len(gifts)):
#             if gifts[i] == gift:
#                 gifts[i] = "None"

#     elif command_type == "Required":
#         gift = command_parts[1]
#         index = int(command_parts[2])
#         if 0 <= index < len(gifts):
#             gifts[index] = gift

#     elif command_type == "JustInCase":
#         gift = command_parts[1]
#         gifts[-1] = gift

#     command = input()

# final_gifts = [gift for gift in gifts if gift != "None"]
# print(" ".join(final_gifts))
