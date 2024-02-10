def mu_online():
    dead = False
    health = 100
    bitcoins = 0
    best_room = 0
    dungeon_rooms = input().split("|")

    for current_room in dungeon_rooms:
        best_room += 1
        data = current_room.split(" ")
        command, number = data[0], int(data[1])

        if command == "potion":
            value_to_heal = number
            if value_to_heal + health <= 100:
                healed_amount = value_to_heal
            else:
                healed_amount = 100 - health
            health += healed_amount
            print(f"You healed for {healed_amount} hp.\n"
                  f"Current health: {health} hp.")

        elif command == "chest":
            bitcoins_amount = number
            bitcoins += bitcoins_amount
            print(f"You found {bitcoins_amount} bitcoins.")

        else:
            monster = command
            monster_attack = number
            health -= monster_attack
            if health > 0:
                print(f"You slayed {monster}.")
            else:
                print(f"You died! Killed by {monster}.")
                print(f"Best room: {best_room}")
                dead = True
                break

    if not dead:
        print("You've made it!\n"
              f"Bitcoins: {bitcoins}\n"
              f"Health: {health}")


mu_online()
