def is_valid_index(lst, indx):
    return 0 <= indx < len(lst)


pirate_ship_status = [int(x) for x in input().split('>')]
warship_status = [int(x) for x in input().split('>')]
maximum_health_capacity = int(input())
enemy_ship_sunk = False
pirate_ship_sunk = False
twenty_percent_of_maximum_health_capacity = maximum_health_capacity * 0.2

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
        if is_valid_index(warship_status, fire_index):
            warship_status[fire_index] -= fire_damage
            if warship_status[fire_index] <= 0:
                print("You won! The enemy ship has sunken.")
                enemy_ship_sunk = True

    elif action == "Defend":
        start_index, end_index, defend_damage = int(info[1]), int(info[2]), int(info[3])
        if is_valid_index(pirate_ship_status, start_index) and is_valid_index(pirate_ship_status, end_index):
            for i in range(start_index, end_index + 1):
                pirate_ship_status[i] -= defend_damage
                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    pirate_ship_sunk = True
                    break

    elif action == "Repair":
        index_repair, health = int(info[1]), int(info[2])
        if is_valid_index(pirate_ship_status, index_repair):
            if pirate_ship_status[index_repair] + health <= maximum_health_capacity:
                pirate_ship_status[index_repair] += health
            else:
                pirate_ship_status[index_repair] = maximum_health_capacity

    elif action == "Status":
        number_section_need_to_repair = 0
        for section in pirate_ship_status:
            if section < twenty_percent_of_maximum_health_capacity:
                number_section_need_to_repair += 1

        print(f"{number_section_need_to_repair} sections need repair.")

if not pirate_ship_sunk and not enemy_ship_sunk:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
