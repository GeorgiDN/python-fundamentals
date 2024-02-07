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
