def fill_the_heroes_data(heroes_data_, num_of_rows):
    for _ in range(num_of_rows):
        hero = input().split()
        name, hp, mp = hero[0], int(hero[1]), int(hero[2])
        heroes_data_[name] = [hp, mp]  # 0: HP,  1: MP
    return heroes_data_


def cast_spell(heroes_data_, name, mana_points, name_to_spell):
    if heroes_data_[name][1] >= mana_points:
        heroes_data_[name][1] -= mana_points
        mana_points_left = heroes_data_[name][1]
        print(f"{name} has successfully cast {name_to_spell} and now has {mana_points_left} MP!")
    else:
        print(f"{name} does not have enough MP to cast {name_to_spell}!")
    return heroes_data_


def take_damage(heroes_data_, name, dmg, atcker):
    heroes_data_[name][0] -= dmg
    if heroes_data_[name][0] > 0:
        curr_hp = heroes_data_[name][0]
        print(f"{name} was hit for {dmg} HP by {atcker} and now has {curr_hp} HP left!")
    else:
        del heroes_data_[name]
        print(f"{name} has been killed by {atcker}!")
    return heroes_data_


def recharge(heroes_data_, name, curr_amount, max_mp):
    if heroes_data_[name][1] + curr_amount <= max_mp:
        amount_mp_recovered = curr_amount
    else:
        amount_mp_recovered = max_mp - heroes_data_[name][1]
    heroes_data_[name][1] += amount_mp_recovered
    print(f"{name} recharged for {amount_mp_recovered} MP!")
    return heroes_data_


def heal(heroes_data_, name, curr_amount, max_hp):
    if heroes_data_[name][0] + curr_amount <= max_hp:
        amount_hp_recovered = curr_amount
    else:
        amount_hp_recovered = max_hp - heroes_data_[name][0]
    heroes_data_[name][0] += amount_hp_recovered
    print(f"{name} healed for {amount_hp_recovered} HP!")
    return heroes_data_


def print_result(heroes_data_):
    result = ''
    for hero, hero_info in heroes_data_.items():
        result += f"{hero}\n"
        hp_points, mp_points = hero_info[0], hero_info[1]
        result += f"  HP: {hp_points}\n"
        result += f"  MP: {mp_points}\n"
    result = result[:-1]
    return print(result)


def main():
    MAX_HP, MAX_MP = 100, 200
    heroes_data = {}
    rows = int(input())
    heroes_data = fill_the_heroes_data(heroes_data, rows)

    while True:
        command = input()
        if command == "End":
            break

        data = command.split(" - ")
        command = data[0]

        if command == "CastSpell":
            hero_name, mana_needed, spell_name = data[1], int(data[2]), data[3]
            heroes_data = cast_spell(heroes_data, hero_name, mana_needed, spell_name)

        elif command == "TakeDamage":
            hero_name, damage, attacker = data[1], int(data[2]), data[3]
            heroes_data = take_damage(heroes_data, hero_name, damage, attacker)

        elif command == "Recharge":
            hero_name, amount = data[1], int(data[2])
            heroes_data = recharge(heroes_data, hero_name, amount, MAX_MP)

        elif command == "Heal":
            hero_name, amount = data[1], int(data[2])
            heroes_data = heal(heroes_data, hero_name, amount, MAX_HP)

    print_result(heroes_data)


if __name__ == '__main__':
    main()




################################################################################
# class HeroOfCodeAndLogicVII:
#     def __init__(self):
#         self.number_of_heroes = 0
#         self.heroes_data = {}
# 
#     def take_integer_input(self):
#         self.number_of_heroes = int(input())
#         return self.number_of_heroes
# 
#     def fill_heroes_data(self):
#         for _ in range(self.number_of_heroes):
#             hero_info = input().split(" ")
#             hero_name, HP, MP = hero_info[0], int(hero_info[1]), int(hero_info[2])
# 
#             if hero_name not in self.heroes_data:
#                 self.heroes_data[hero_name] = [HP, MP]
# 
#         return self.heroes_data
# 
#     def castspell(self, hero, mp, sp_name, heroes_data):
#         if hero in heroes_data:
#             if mp <= heroes_data[hero][1]:
#                 heroes_data[hero][1] -= mp
#                 mp_left = heroes_data[hero][1]
#                 print(f"{hero} has successfully cast {sp_name} and now has {mp_left} MP!")
#             else:
#                 print(f"{hero} does not have enough MP to cast {sp_name}!")
# 
#         return heroes_data
# 
#     def take_damage(self, hero, dmg, atcker, heroes_data):
#         if hero in heroes_data:
#             heroes_data[hero][0] -= dmg
#             hp_left = heroes_data[hero][0]
#             if hp_left > 0:
#                 print(f"{hero} was hit for {dmg} HP by {atcker} and now has {hp_left} HP left!")
#             else:
#                 del heroes_data[hero]
#                 print(f"{hero} has been killed by {atcker}!")
# 
#         return heroes_data
# 
#     def recharge(self, hero, amount, heroes_data):
#         if hero in heroes_data:
#             if heroes_data[hero][1] + amount <= 200:
#                 heroes_data[hero][1] += amount
#                 print(f"{hero} recharged for {amount} MP!")
#             else:
#                 diff_mp = 200 - heroes_data[hero][1]
#                 heroes_data[hero][1] = 200
#                 print(f"{hero} recharged for {diff_mp} MP!")
# 
#         return heroes_data
# 
#     def heal(self, hero, amount, heroes_data):
#         if hero in heroes_data:
#             if heroes_data[hero][0] + amount <= 100:
#                 heroes_data[hero][0] += amount
#                 print(f"{hero} healed for {amount} HP!")
#             else:
#                 diff_hp = 100 - heroes_data[hero][0]
#                 heroes_data[hero][0] = 100
#                 print(f"{hero} healed for {diff_hp} HP!")
# 
#         return heroes_data
# 
#     def play_heroes_of_god_and_logic(self):
#         while True:
#             command = input()
#             if command == "End":
#                 break
# 
#             # {'Solmyr': [85, 120], 'Kyrre': [99, 50]}
#             info = command.split(" - ")
#             if info[0] == "CastSpell":
#                 hero_cast_spell, mp_needed, spell_name = info[1], int(info[2]), info[3]
#                 self.castspell(hero_cast_spell, mp_needed, spell_name, self.heroes_data)
# 
#             elif info[0] == "TakeDamage":
#                 hero_take_damage, damage, attacker = info[1], int(info[2]), info[3]
#                 self.take_damage(hero_take_damage, damage, attacker, self.heroes_data)
# 
#             elif info[0] == "Recharge":
#                 hero_recharge, amount_recharge = info[1], int(info[2])
#                 self.recharge(hero_recharge, amount_recharge, self.heroes_data)
# 
#             elif info[0] == "Heal":
#                 hero_heal, amount_heal = info[1], int(info[2])
#                 self.heal(hero_heal, amount_heal, self.heroes_data)
# 
#         return self.heroes_data
# 
#     def print_final_result(self):
#         for name_, data in self.heroes_data.items():
#             hp_ = data[0]
#             mp_ = data[1]
#             print(f"{name_}\n"
#                   f"  HP: {hp_}\n"
#                   f"  MP: {mp_}")
# 
# 
# hero_of_code_and_logic_8 = HeroOfCodeAndLogicVII()
# hero_of_code_and_logic_8.take_integer_input()
# hero_of_code_and_logic_8.fill_heroes_data()
# hero_of_code_and_logic_8.play_heroes_of_god_and_logic()
# hero_of_code_and_logic_8.print_final_result()




################################################################################
# def take_integer_input():
#     return int(input())
# 
# 
# def fill_heroes_data(num):
#     heroes_data = {}
#     for _ in range(num):
#         hero_info = input().split(" ")
#         hero_name, HP, MP = hero_info[0], int(hero_info[1]), int(hero_info[2])
# 
#         if hero_name not in heroes_data:
#             heroes_data[hero_name] = [HP, MP]
# 
#     return heroes_data
# 
# 
# def castspell(hero, mp, sp_name, heroes_data):
#     if hero in heroes_data:
#         if mp <= heroes_data[hero][1]:
#             heroes_data[hero][1] -= mp
#             mp_left = heroes_data[hero][1]
#             print(f"{hero} has successfully cast {sp_name} and now has {mp_left} MP!")
#         else:
#             print(f"{hero} does not have enough MP to cast {sp_name}!")
# 
#     return heroes_data
# 
# 
# def take_damage(hero, dmg, atcker, heroes_data):
#     if hero in heroes_data:
#         heroes_data[hero][0] -= dmg
#         hp_left = heroes_data[hero][0]
#         if hp_left > 0:
#             print(f"{hero} was hit for {dmg} HP by {atcker} and now has {hp_left} HP left!")
#         else:
#             del heroes_data[hero]
#             print(f"{hero} has been killed by {atcker}!")
# 
#     return heroes_data
# 
# 
# def recharge(hero, amount, heroes_data):
#     if hero in heroes_data:
#         if heroes_data[hero][1] + amount <= 200:
#             heroes_data[hero][1] += amount
#             print(f"{hero} recharged for {amount} MP!")
#         else:
#             diff_mp = 200 - heroes_data[hero][1]
#             heroes_data[hero][1] = 200
#             print(f"{hero} recharged for {diff_mp} MP!")
# 
#     return heroes_data
# 
# 
# def heal(hero, amount, heroes_data):
#     if hero in heroes_data:
#         if heroes_data[hero][0] + amount <= 100:
#             heroes_data[hero][0] += amount
#             print(f"{hero} healed for {amount} HP!")
#         else:
#             diff_hp = 100 - heroes_data[hero][0]
#             heroes_data[hero][0] = 100
#             print(f"{hero} healed for {diff_hp} HP!")
# 
#     return heroes_data
# 
# 
# def play_heroes_of_god_and_logic(heroes_data):
#     while True:
#         command = input()
#         if command == "End":
#             break
# 
#         # {'Solmyr': [85, 120], 'Kyrre': [99, 50]}
#         info = command.split(" - ")
#         if info[0] == "CastSpell":
#             hero_cast_spell, mp_needed, spell_name = info[1], int(info[2]), info[3]
#             castspell(hero_cast_spell, mp_needed, spell_name, heroes_data)
# 
#         elif info[0] == "TakeDamage":
#             hero_take_damage, damage, attacker = info[1], int(info[2]), info[3]
#             take_damage(hero_take_damage, damage, attacker, heroes_data)
# 
#         elif info[0] == "Recharge":
#             hero_recharge, amount_recharge = info[1], int(info[2])
#             recharge(hero_recharge, amount_recharge, heroes_data)
# 
#         elif info[0] == "Heal":
#             hero_heal, amount_heal = info[1], int(info[2])
#             heal(hero_heal, amount_heal, heroes_data)
# 
#     return heroes_data
# 
# 
# def print_final_result(play_game):
#     for name_, data in play_game.items():
#         hp_ = data[0]
#         mp_ = data[1]
#         print(f"{name_}\n"
#               f"  HP: {hp_}\n"
#               f"  MP: {mp_}")
# 
# 
# n = take_integer_input()
# heroes_data_ = fill_heroes_data(n)
# play_game_ = play_heroes_of_god_and_logic(heroes_data_)
# print_final_result(play_game_)




################################################################################
# n = int(input())
# heroes_data = {}
# 
# 
# for _ in range(n):
#     hero_info = input().split(" ")
#     hero_name, HP, MP = hero_info[0], int(hero_info[1]), int(hero_info[2])
# 
#     if hero_name not in heroes_data:
#         heroes_data[hero_name] = {"HP": HP, "MP": MP}
# 
# while True:
#     command = input()
#     if command == "End":
#         break
# 
#     info = command.split(" - ")
#     if info[0] == "CastSpell":
#         hero_cast_spell, mp_needed, spell_name = info[1], int(info[2]), info[3]
#         if hero_cast_spell in heroes_data:
#             if mp_needed <= heroes_data[hero_cast_spell]["MP"]:
#                 heroes_data[hero_cast_spell]["MP"] -= mp_needed
#                 mp_left = heroes_data[hero_cast_spell]["MP"]
#                 print(f"{hero_cast_spell} has successfully cast {spell_name} and now has {mp_left} MP!")
#             else:
#                 print(f"{hero_cast_spell} does not have enough MP to cast {spell_name}!")
# 
#     elif info[0] == "TakeDamage":
#         hero_take_damage, damage, attacker = info[1], int(info[2]), info[3]
#         if hero_take_damage in heroes_data:
#             heroes_data[hero_take_damage]["HP"] -= damage
#             hp_left = heroes_data[hero_take_damage]["HP"]
#             if hp_left > 0:
#                 print(f"{hero_take_damage} was hit for {damage} HP by {attacker} and now has {hp_left} HP left!")
#             else:
#                 del heroes_data[hero_take_damage]
#                 print(f"{hero_take_damage} has been killed by {attacker}!")
# 
#     elif info[0] == "Recharge":
#         hero_recharge, amount_recharge = info[1], int(info[2])
#         if hero_recharge in heroes_data:
#             if heroes_data[hero_recharge]["MP"] + amount_recharge <= 200:
#                 heroes_data[hero_recharge]["MP"] += amount_recharge
#                 print(f"{hero_recharge} recharged for {amount_recharge} MP!")
#             else:
#                 diff_mp = 200 - heroes_data[hero_recharge]["MP"]
#                 heroes_data[hero_recharge]["MP"] = 200
#                 print(f"{hero_recharge} recharged for {diff_mp} MP!")
# 
#     elif info[0] == "Heal":
#         hero_heal, amount_heal = info[1], int(info[2])
#         if hero_heal in heroes_data:
#             if heroes_data[hero_heal]["HP"] + amount_heal <= 100:
#                 heroes_data[hero_heal]["HP"] += amount_heal
#                 print(f"{hero_heal} healed for {amount_heal} HP!")
#             else:
#                 diff_hp = 100 - heroes_data[hero_heal]["HP"]
#                 heroes_data[hero_heal]["HP"] = 100
#                 print(f"{hero_heal} healed for {diff_hp} HP!")
# 
# 
# for name_, data in heroes_data.items():
#     hp_ = data["HP"]
#     mp_ = data["MP"]
#     print(f"{name_}\n"
#           f"  HP: {hp_}\n"
#           f"  MP: {mp_}")

