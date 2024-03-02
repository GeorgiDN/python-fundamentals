def check_values(damage, health, armour):
    if not damage.isdigit():
        damage = 45
    if not health.isdigit():
        health = 250
    if not armour.isdigit():
        armour = 10

    return int(damage), int(health), int(armour)


def take_the_information(dragons_data, color, name, damage, health, armour):
    if color not in dragons_data:
        dragons_data[color] = {}

    if name not in dragons_data[color]:
        dragons_data[color][name] = []
        dragons_data[color][name].append(damage)
        dragons_data[color][name].append(health)
        dragons_data[color][name].append(armour)

    else:
        if name in dragons_data[color]:
            dragons_data[color][name] = []
            dragons_data[color][name].append(damage)
            dragons_data[color][name].append(health)
            dragons_data[color][name].append(armour)

    return dragons_data


def print_result(dragons_data):
    for type_, names_data in dragons_data.items():
        damages = []
        healths = []
        armours = []
        name_info = []

        for curr_name, info in names_data.items():
            curr_damage, curr_health, curr_armour = info[0], info[1], info[2]
            damages.append(curr_damage)
            healths.append(curr_health)
            armours.append(curr_armour)
            name_info.append(f"-{curr_name} -> damage: {curr_damage}, health: {curr_health}, armor: {curr_armour}")

        average_damage = sum(damages) / len(damages)
        average_health = sum(healths) / len(healths)
        average_armour = sum(armours) / len(armours)

        print(f"{type_}::({average_damage:.2f}/{average_health:.2f}/{average_armour:.2f})")
        print('\n'.join(name_info))


def main():
    dragons_data = {}
    rows = int(input())

    for _ in range(rows):
        data = input().split()
        color, name, damage, health, armour = data[0], data[1], data[2], data[3], data[4]
        damage, health, armour = check_values(damage, health, armour)
        dragons_data = take_the_information(dragons_data, color, name, damage, health, armour)

    for color, dragon_names in dragons_data.items():
        dragons_data[color] = dict(sorted(dragon_names.items()))

    print_result(dragons_data)


if __name__ == "__main__":
    main()

