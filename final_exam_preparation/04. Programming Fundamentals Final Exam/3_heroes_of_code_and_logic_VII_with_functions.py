def take_integer_input():
    return int(input())


def fill_heroes_data(num):
    heroes_data = {}
    for _ in range(num):
        hero_info = input().split(" ")
        hero_name, HP, MP = hero_info[0], int(hero_info[1]), int(hero_info[2])

        if hero_name not in heroes_data:
            heroes_data[hero_name] = [HP, MP]

    return heroes_data


def castspell(hero, mp, sp_name, heroes_data):
    if hero in heroes_data:
        if mp <= heroes_data[hero][1]:
            heroes_data[hero][1] -= mp
            mp_left = heroes_data[hero][1]
            print(f"{hero} has successfully cast {sp_name} and now has {mp_left} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {sp_name}!")

    return heroes_data


def take_damage(hero, dmg, atcker, heroes_data):
    if hero in heroes_data:
        heroes_data[hero][0] -= dmg
        hp_left = heroes_data[hero][0]
        if hp_left > 0:
            print(f"{hero} was hit for {dmg} HP by {atcker} and now has {hp_left} HP left!")
        else:
            del heroes_data[hero]
            print(f"{hero} has been killed by {atcker}!")

    return heroes_data


def recharge(hero, amount, heroes_data):
    if hero in heroes_data:
        if heroes_data[hero][1] + amount <= 200:
            heroes_data[hero][1] += amount
            print(f"{hero} recharged for {amount} MP!")
        else:
            diff_mp = 200 - heroes_data[hero][1]
            heroes_data[hero][1] = 200
            print(f"{hero} recharged for {diff_mp} MP!")

    return heroes_data


def heal(hero, amount, heroes_data):
    if hero in heroes_data:
        if heroes_data[hero][0] + amount <= 100:
            heroes_data[hero][0] += amount
            print(f"{hero} healed for {amount} HP!")
        else:
            diff_hp = 100 - heroes_data[hero][0]
            heroes_data[hero][0] = 100
            print(f"{hero} healed for {diff_hp} HP!")

    return heroes_data


def play_heroes_of_god_and_logic(heroes_data):
    while True:
        command = input()
        if command == "End":
            break

        info = command.split(" - ")
        if info[0] == "CastSpell":
            hero_cast_spell, mp_needed, spell_name = info[1], int(info[2]), info[3]
            castspell(hero_cast_spell, mp_needed, spell_name, heroes_data)

        elif info[0] == "TakeDamage":
            hero_take_damage, damage, attacker = info[1], int(info[2]), info[3]
            take_damage(hero_take_damage, damage, attacker, heroes_data)

        elif info[0] == "Recharge":
            hero_recharge, amount_recharge = info[1], int(info[2])
            recharge(hero_recharge, amount_recharge, heroes_data)

        elif info[0] == "Heal":
            hero_heal, amount_heal = info[1], int(info[2])
            heal(hero_heal, amount_heal, heroes_data)

    return heroes_data


def print_final_result(play_game):
    for name_, data in play_game.items():
        hp_ = data[0]
        mp_ = data[1]
        print(f"{name_}\n"
              f"  HP: {hp_}\n"
              f"  MP: {mp_}")


n = take_integer_input()
heroes_data_ = fill_heroes_data(n)
play_game_ = play_heroes_of_god_and_logic(heroes_data_)
print_final_result(play_game_)
