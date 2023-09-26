events_input_list = input().split('|')

total_energy = 100
total_coins = 100
gained_energy = 0
unclosed_condition = True

for event in events_input_list:
    event_info = event.split("-")
    event_type = event_info[0]
    event_value = int(event_info[1])

    if event_type == 'rest':
        curr_energy = event_value
        if total_energy == 100:
            curr_energy = 0
        total_energy += curr_energy

        if total_energy > 100:
            total_energy = 100
        print(f"You gained {curr_energy} energy.")
        print(f'Current energy: {total_energy}.')

    elif event_type == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")

    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            unclosed_condition = False
            break

if unclosed_condition:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
