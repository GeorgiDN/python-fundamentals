# With Nested dictionary
n = int(input())
heroes_data = {}


for _ in range(n):
    hero_info = input().split(" ")
    hero_name, HP, MP = hero_info[0], int(hero_info[1]), int(hero_info[2])

    if hero_name not in heroes_data:
        heroes_data[hero_name] = {"HP": HP, "MP": MP}

while True:
    command = input()
    if command == "End":
        break

    info = command.split(" - ")
    if info[0] == "CastSpell":
        hero_cast_spell, mp_needed, spell_name = info[1], int(info[2]), info[3]
        if hero_cast_spell in heroes_data:
            if mp_needed <= heroes_data[hero_cast_spell]["MP"]:
                heroes_data[hero_cast_spell]["MP"] -= mp_needed
                mp_left = heroes_data[hero_cast_spell]["MP"]
                print(f"{hero_cast_spell} has successfully cast {spell_name} and now has {mp_left} MP!")
            else:
                print(f"{hero_cast_spell} does not have enough MP to cast {spell_name}!")

    elif info[0] == "TakeDamage":
        hero_take_damage, damage, attacker = info[1], int(info[2]), info[3]
        if hero_take_damage in heroes_data:
            heroes_data[hero_take_damage]["HP"] -= damage
            hp_left = heroes_data[hero_take_damage]["HP"]
            if hp_left > 0:
                print(f"{hero_take_damage} was hit for {damage} HP by {attacker} and now has {hp_left} HP left!")
            else:
                del heroes_data[hero_take_damage]
                print(f"{hero_take_damage} has been killed by {attacker}!")

    elif info[0] == "Recharge":
        hero_recharge, amount_recharge = info[1], int(info[2])
        if hero_recharge in heroes_data:
            if heroes_data[hero_recharge]["MP"] + amount_recharge <= 200:
                heroes_data[hero_recharge]["MP"] += amount_recharge
                print(f"{hero_recharge} recharged for {amount_recharge} MP!")
            else:
                diff_mp = 200 - heroes_data[hero_recharge]["MP"]
                heroes_data[hero_recharge]["MP"] = 200
                print(f"{hero_recharge} recharged for {diff_mp} MP!")

    elif info[0] == "Heal":
        hero_heal, amount_heal = info[1], int(info[2])
        if hero_heal in heroes_data:
            if heroes_data[hero_heal]["HP"] + amount_heal <= 100:
                heroes_data[hero_heal]["HP"] += amount_heal
                print(f"{hero_heal} healed for {amount_heal} HP!")
            else:
                diff_hp = 100 - heroes_data[hero_heal]["HP"]
                heroes_data[hero_heal]["HP"] = 100
                print(f"{hero_heal} healed for {diff_hp} HP!")


for name_, data in heroes_data.items():
    hp_ = data["HP"]
    mp_ = data["MP"]
    print(f"{name_}\n"
          f"  HP: {hp_}\n"
          f"  MP: {mp_}")





################################################   Task Description   ################################################
# Problem 3 - Heroes of Code and Logic VII
#
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.
#
# You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic.
# You want to play it all day long! So cancel all other arrangements and create your party!
# On the first line of the standard input, you will receive an integer n – the number of heroes that you can
# choose for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points
# separated by a single space in the following format:
# "{hero name} {HP} {MP}"
#     - HP stands for hit points and MP for mana points
#     - a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game.
# You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
#     • If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
#         o "{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
#     • If the hero is unable to cast the spell print:
#         o "{hero name} does not have enough MP to cast {spell name}!"
#           "TakeDamage – {hero name} – {damage} – {attacker}"
#     • Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
#         o "{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
#     • If the hero has died, remove him from your party and print:
#         o "{hero name} has been killed by {attacker}!"
#           "Recharge – {hero name} – {amount}"
#     • The hero increases his MP. If it brings the MP of the hero above the maximum value (200),
#       MP is increased to 200. (the MP can't go over the maximum value).
#     • Print the following message:
#         o "{hero name} recharged for {amount recovered} MP!"
#           "Heal – {hero name} – {amount}"
#     • The hero increases his HP. If a command is given that would bring the HP of the hero above
#       the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
#     • Print the following message:
#         o "{hero name} healed for {amount recovered} HP!"
# Input
#     • On the first line of the standard input, you will receive an integer n
#     • On the following n lines, the heroes themselves will follow with their hit points and mana points
#       separated by a space in the following format:
#       "{hero name} {HP} {MP}"
#     • You will be receiving different commands, each on a new line, separated by " – ",
#       until the "End" command is given
# Output
#     • Print all members of your party who are still alive,
#       in the following format (their HP/MP need to be indented 2 spaces):
#       "{hero name}
#         HP: {current HP}
#         MP: {current MP}"
# Constraints
#     • The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative
#       or exceed the respective limits.
#     • The HP/MP amounts in the commands will never be negative.
#     • The hero names in the commands will always be valid members of your party. No need to check that explicitly.

  
