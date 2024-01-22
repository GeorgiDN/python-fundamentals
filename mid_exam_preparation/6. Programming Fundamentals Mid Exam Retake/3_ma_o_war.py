def is_valid_index(lst, indx):
    return 0 <= indx < len(lst)


def take_ship_status():
    return [int(x) for x in input().split('>')]


def take_maximum_health_capacity():
    return int(input())


def take_percent_of_maximum_health_capacity(max_h_capacity):
    return max_h_capacity * 0.2


def fire(idx, damage, ship):
    global enemy_ship_sunk
    if is_valid_index(ship, idx):
        ship[idx] -= damage
        if ship[idx] <= 0:
            enemy_ship_sunk = True
            return print("You won! The enemy ship has sunken.")
    return ship


def defend(start_idx, end_idx, damage, ship):
    global enemy_ship_sunk
    if is_valid_index(ship, start_idx) and is_valid_index(ship, end_idx):
        for i in range(start_idx, end_idx + 1):
            ship[i] -= damage
            if ship[i] <= 0:
                enemy_ship_sunk = True
                return print("You lost! The pirate ship has sunken.")
    return ship


def repair(idx_repair, health_, ship, max_health):
    if is_valid_index(ship, idx_repair):
        if ship[idx_repair] + health_ <= max_health:
            ship[idx_repair] += health_
        else:
            ship[idx_repair] = max_health
    return ship


def take_status(ship, percent):
    counter = len([section for section in ship if section < percent])
    print(f"{counter} sections need repair.")


def print_pirate_ship_status(ship):
    print(f"Pirate ship status: {sum(ship)}")


def print_warship_status(ship):
    print(f"Warship status: {sum(ship)}")


def implement_the_war(war_ship, pirate_ship):
    global pirate_ship_sunk
    global enemy_ship_sunk

    while True:
        if pirate_ship_sunk or enemy_ship_sunk:
            break

        command = input()
        if command == "Retire":
            break

        info = command.split(" ")
        action = info[0]

        if action == "Fire":
            fire_index, fire_damage = int(info[1]), int(info[2])
            war_ship = fire(fire_index, fire_damage, war_ship)

        elif action == "Defend":
            start_index, end_index, defend_damage = int(info[1]), int(info[2]), int(info[3])
            pirate_ship = defend(start_index, end_index, defend_damage, pirate_ship)

        elif action == "Repair":
            index_repair, health = int(info[1]), int(info[2])
            pirate_ship = repair(index_repair, health, pirate_ship, maximum_health_capacity)

        elif action == "Status":
            take_status(pirate_ship, twenty_percent_of_maximum_health_capacity)

    return war_ship, pirate_ship


pirate_ship_status = take_ship_status()
warship_status = take_ship_status()
maximum_health_capacity = take_maximum_health_capacity()
enemy_ship_sunk = False
pirate_ship_sunk = False
twenty_percent_of_maximum_health_capacity = take_percent_of_maximum_health_capacity(maximum_health_capacity)
implement_the_war(warship_status, pirate_ship_status)

if not pirate_ship_sunk and not enemy_ship_sunk:
    print_pirate_ship_status(pirate_ship_status)
    print_warship_status(warship_status)








##
# def is_valid_index(lst, indx):
#     return 0 <= indx < len(lst)


# pirate_ship_status = [int(x) for x in input().split('>')]
# warship_status = [int(x) for x in input().split('>')]
# maximum_health_capacity = int(input())
# enemy_ship_sunk = False
# pirate_ship_sunk = False
# twenty_percent_of_maximum_health_capacity = maximum_health_capacity * 0.2

# while True:
#     if pirate_ship_sunk or enemy_ship_sunk:
#         break

#     command = input()
#     if command == "Retire":
#         break

#     info = command.split(" ")
#     action = info[0]

#     if action == "Fire":
#         fire_index, fire_damage = int(info[1]), int(info[2])
#         if is_valid_index(warship_status, fire_index):
#             warship_status[fire_index] -= fire_damage
#             if warship_status[fire_index] <= 0:
#                 print("You won! The enemy ship has sunken.")
#                 enemy_ship_sunk = True

#     elif action == "Defend":
#         start_index, end_index, defend_damage = int(info[1]), int(info[2]), int(info[3])
#         if is_valid_index(pirate_ship_status, start_index) and is_valid_index(pirate_ship_status, end_index):
#             for i in range(start_index, end_index + 1):
#                 pirate_ship_status[i] -= defend_damage
#                 if pirate_ship_status[i] <= 0:
#                     print("You lost! The pirate ship has sunken.")
#                     pirate_ship_sunk = True
#                     break

#     elif action == "Repair":
#         index_repair, health = int(info[1]), int(info[2])
#         if is_valid_index(pirate_ship_status, index_repair):
#             if pirate_ship_status[index_repair] + health <= maximum_health_capacity:
#                 pirate_ship_status[index_repair] += health
#             else:
#                 pirate_ship_status[index_repair] = maximum_health_capacity

#     elif action == "Status":
#         number_section_need_to_repair = 0
#         for section in pirate_ship_status:
#             if section < twenty_percent_of_maximum_health_capacity:
#                 number_section_need_to_repair += 1

#         print(f"{number_section_need_to_repair} sections need repair.")

if not pirate_ship_sunk and not enemy_ship_sunk:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
