max_energy = 100
total_energy = 100
total_coins = 100
events = input().split("|")
closed = False

for ingredient in events:
    info = ingredient.split("-")
    if info[0] == "rest":
        energy = int(info[1])
        if total_energy == max_energy:
            gained_energy = 0
        else:
            gained_energy = energy
            if total_energy + energy > max_energy:
                gained_energy = max_energy - total_energy
        total_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif info[0] == "order":
        coins = int(info[1])
        if total_energy >= 30:
            total_energy -= 30
            total_coins += coins
            print(f"You earned {coins} coins.")
        else:
            total_energy += 50
            print("You had to rest!")

    else:
        ingredient, coins = info[0], int(info[1])
        if total_coins >= coins:
            total_coins -= coins
            print(f"You bought {ingredient}.")
        else:
            closed = True
            print(f"Closed! Cannot afford {ingredient}.")
            break

if not closed:
    print(f"Day completed!\n"
          f"Coins: {total_coins}\n"
          f"Energy: {total_energy}"
          )



# events_input_list = input().split('|')

# total_energy = 100
# total_coins = 100
# gained_energy = 0
# unclosed_condition = True

# for event in events_input_list:
#     event_info = event.split("-")
#     event_type = event_info[0]
#     event_value = int(event_info[1])

#     if event_type == 'rest':
#         curr_energy = event_value
#         if total_energy == 100:
#             curr_energy = 0
#         total_energy += curr_energy

#         if total_energy > 100:
#             total_energy = 100
#         print(f"You gained {curr_energy} energy.")
#         print(f'Current energy: {total_energy}.')

#     elif event_type == 'order':
#         if total_energy >= 30:
#             total_energy -= 30
#             total_coins += event_value
#             print(f"You earned {event_value} coins.")
#         else:
#             total_energy += 50
#             print(f"You had to rest!")

#     else:
#         if total_coins >= event_value:
#             total_coins -= event_value
#             print(f"You bought {event_type}.")
#         else:
#             print(f"Closed! Cannot afford {event_type}.")
#             unclosed_condition = False
#             break

# if unclosed_condition:
#     print("Day completed!")
#     print(f"Coins: {total_coins}")
#     print(f"Energy: {total_energy}")
