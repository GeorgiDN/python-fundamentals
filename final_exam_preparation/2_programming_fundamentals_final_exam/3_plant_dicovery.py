n = int(input())
plants = {}

for i in range(n):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])

    if plant not in plants:
        plants[plant] = {'rarity': rarity, 'ratings': []}

while True:
    command = input()
    if command == 'Exhibition':
        break
    else:
        tokens = command.split(": ")
        action = tokens[0]

        if action == 'Rate':
            plant_information = tokens[1]
            plant_info = plant_information.split(' - ')
            plant_name = plant_info[0]
            rating = int(plant_info[1])

            if plant_name in plants:
                plants[plant_name]['ratings'].append(rating)
            else:
                print("error")

        elif action == 'Update':
            update_information = tokens[1]
            update_info = update_information.split(' - ')
            plant_name = update_info[0]
            new_rarity = int(update_info[1])

            if plant_name in plants:
                plants[plant_name]['rarity'] = new_rarity
            else:
                print("error")

        elif action == 'Reset':
            plant_name = tokens[1]

            if plant_name in plants:
                plants[plant_name]['ratings'] = []
            else:
                print("error")

for plant, data in plants.items():
    rarity = data['rarity']
    ratings = data['ratings']

    if ratings:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = 0

    plants[plant] = {'rarity': rarity, 'average_rating': average_rating}


print("Plants for the exhibition:")
for plant, data in plants.items():
    rarity = data['rarity']
    average_rating = data['average_rating']
    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
