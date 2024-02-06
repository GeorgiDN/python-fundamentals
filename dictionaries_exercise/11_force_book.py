def side_user(force_users, side, user, reg_users):
    if side not in force_users:
        force_users[side] = []
    if user not in reg_users:
        force_users[side].append(user)
        reg_users.append(user)

    return force_users, reg_users


def user_side(force_users, user, side, reg_users):
    if side not in force_users:
        force_users[side] = []
    if user not in reg_users:
        force_users[side].append(user)
        reg_users.append(user)
    if force_users:
        if user in reg_users:
            for curr_side, data_ in force_users.items():
                if data_:
                    for usr in data_:
                        if usr == user:
                            force_users[curr_side].remove(user)
                            force_users[side].append(user)

    print(f"{user} joins the {side} side!")
    return force_users, reg_users


def force_book():
    force_users_info = {}
    registered_users = []
    while True:
        command = input()
        if command == "Lumpawaroo":
            break

        data = command.split(" ")
        if "|" in data:
            info = command.split(" | ")
            force_side, force_user = info[0], info[1]
            force_users_info, registered_users = side_user(force_users_info, force_side, force_user, registered_users)

        elif "->" in data:
            info = command.split(" -> ")
            force_user, force_side = info[0], info[1]
            force_users_info, registered_users = user_side(force_users_info, force_user, force_side, registered_users)

    for current_side, users_data in force_users_info.items():
        if users_data:
            members = len(users_data)
            print(f"Side: {current_side}, Members: {members}")
            for current_user in users_data:
                print(f"! {current_user}")


force_book()





# sides = {}
# users = []
# command = input()
# while command != "Lumpawaroo":
#     if "|" in command:
#         force_side = command.split(" | ")[0]
#         force_user = command.split(" | ")[1]
#         if force_user not in users:
#             users.append(force_user)
#             if force_side not in sides:
#                 sides[force_side] = []
#             sides[force_side].append(force_user)
#     elif "->" in command:
#         force_side = command.split(" -> ")[1]
#         force_user = command.split(" -> ")[0]
#         if force_user in users:
#             if force_side not in sides:
#                 sides[force_side] = []
#             sides[force_side].append(force_user)
#             for key, value in sides.items():
#                 if key != force_side and force_user in value:
#                     sides[key].remove(force_user)
#         else:
#             users.append(force_user)
#             if force_side not in sides:
#                 sides[force_side] = []
#             sides[force_side].append(force_user)
#         print(f"{force_user} joins the {force_side} side!")
#     command = input()
# for force_sides, force_users in sides.items():
#     if len(force_users) > 0:
#         print(f"Side: {force_sides}, Members: {len(force_users)}")
#         for member in force_users:
#             print(f"! {member}")
          
