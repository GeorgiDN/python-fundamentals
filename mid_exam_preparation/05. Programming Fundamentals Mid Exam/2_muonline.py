def potion(health_, value_to_heal):
    if value_to_heal + health_ <= 100:
        healed_amount = value_to_heal
    else:
        healed_amount = 100 - health_
    health_ += healed_amount
    print(f"You healed for {healed_amount} hp.\n"
          f"Current health: {health_} hp.")
    return health_


def chest(total_bitcoins, bitcoins_found):
    total_bitcoins += bitcoins_found
    print(f"You found {bitcoins_found} bitcoins.")
    return total_bitcoins


def attack(health_, curr_monster, curr_monster_attack, rooms, dead):
    health_ -= curr_monster_attack
    if health_ > 0:
        print(f"You slayed {curr_monster}.")
    else:
        print(f"You died! Killed by {curr_monster}.")
        print(f"Best room: {rooms}")
        dead = True
    return health_, dead


def mu_online():
    is_dead = False
    health = 100
    bitcoins = 0
    best_room = 0
    dungeon_rooms = input().split("|")

    for current_room in dungeon_rooms:
        best_room += 1
        if is_dead:
            break
        data = current_room.split(" ")
        command, number = data[0], int(data[1])

        if command == "potion":
            heal_value = number
            health = potion(health, heal_value)

        elif command == "chest":
            bitcoins_amount = number
            bitcoins = chest(bitcoins, bitcoins_amount)

        else:
            monster = command
            monster_attack = number
            health, is_dead = attack(health, monster, monster_attack, best_room, is_dead)

    if not is_dead:
        print("You've made it!\n"
              f"Bitcoins: {bitcoins}\n"
              f"Health: {health}")


mu_online()




# def mu_online():
#     dead = False
#     health = 100
#     bitcoins = 0
#     best_room = 0
#     dungeon_rooms = input().split("|")
#
#     for current_room in dungeon_rooms:
#         best_room += 1
#         data = current_room.split(" ")
#         command, number = data[0], int(data[1])
#
#         if command == "potion":
#             value_to_heal = number
#             if value_to_heal + health <= 100:
#                 healed_amount = value_to_heal
#             else:
#                 healed_amount = 100 - health
#             health += healed_amount
#             print(f"You healed for {healed_amount} hp.\n"
#                   f"Current health: {health} hp.")
#
#         elif command == "chest":
#             bitcoins_amount = number
#             bitcoins += bitcoins_amount
#             print(f"You found {bitcoins_amount} bitcoins.")
#
#         else:
#             monster = command
#             monster_attack = number
#             health -= monster_attack
#             if health > 0:
#                 print(f"You slayed {monster}.")
#             else:
#                 print(f"You died! Killed by {monster}.")
#                 print(f"Best room: {best_room}")
#                 dead = True
#                 break
#
#     if not dead:
#         print("You've made it!\n"
#               f"Bitcoins: {bitcoins}\n"
#               f"Health: {health}")
#
#
# mu_online()




# def mu_online():
#     dead = False
#     health = 100
#     bitcoins = 0
#     best_room = 0
#     dungeon_rooms = input().split("|")

#     for current_room in dungeon_rooms:
#         best_room += 1
#         data = current_room.split(" ")
#         command, number = data[0], int(data[1])

#         if command == "potion":
#             value_to_heal = number
#             if value_to_heal + health <= 100:
#                 healed_amount = value_to_heal
#             else:
#                 healed_amount = 100 - health
#             health += healed_amount
#             print(f"You healed for {healed_amount} hp.\n"
#                   f"Current health: {health} hp.")

#         elif command == "chest":
#             bitcoins_amount = number
#             bitcoins += bitcoins_amount
#             print(f"You found {bitcoins_amount} bitcoins.")

#         else:
#             monster = command
#             monster_attack = number
#             health -= monster_attack
#             if health > 0:
#                 print(f"You slayed {monster}.")
#             else:
#                 print(f"You died! Killed by {monster}.")
#                 print(f"Best room: {best_room}")
#                 dead = True
#                 break

#     if not dead:
#         print("You've made it!\n"
#               f"Bitcoins: {bitcoins}\n"
#               f"Health: {health}")


# mu_online()
