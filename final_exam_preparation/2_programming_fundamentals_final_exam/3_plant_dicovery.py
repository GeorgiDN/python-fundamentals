def take_plants_data(plants_data_, rows_):
    for _ in range(rows_):
        plant_, rariry = input().split("<->")
        plants_data_[plant_] = {"rarity": rariry, "ratings": []}
    return plants_data_


def rate(plants_data_, plant_, rating_):
    if plant_ not in plants_data_:
        print("error")
    else:
        plants_data_[plant_]["ratings"].append(rating_)
    return plants_data_


def update_plants_data(plants_data_, plant_, new_rarity_):
    if plant_ not in plants_data_:
        print("error")
    else:
        plants_data_[plant_]["rarity"] = new_rarity_
    return plants_data_


def reset(plants_data_, plant_):
    if plant_ not in plants_data_:
        print("error")
    else:
        plants_data_[plant_]["ratings"].clear()
    return plants_data_


def print_result(plants_data_):
    result = ''
    result += "Plants for the exhibition:\n"

    for curr_plant, plant_information in plants_data_.items():
        rarity = plant_information["rarity"]
        ratings = plant_information["ratings"]
        if ratings:
            average_rating = sum(ratings) / len(ratings)
        else:
            average_rating = 0
        result += f"- {curr_plant}; Rarity: {rarity}; Rating: {average_rating:.2f}\n"
    return print(result)


def main():
    plants_data = {}
    rows = int(input())

    plants_data = take_plants_data(plants_data, rows)

    while True:
        data = input().split(": ")
        command = data[0]

        if command == "Exhibition":
            break

        elif command == "Rate":
            plant_info = data[1].split(" - ")
            plant, rating = plant_info[0], int(plant_info[1])
            plants_data = rate(plants_data, plant, rating)

        elif command == "Update":
            plant_info = data[1].split(" - ")
            plant, new_rarity = plant_info[0], int(plant_info[1])
            plants_data = update_plants_data(plants_data, plant, new_rarity)

        elif command == "Reset":
            plant = data[1]
            plants_data = reset(plants_data, plant)

    print_result(plants_data)


if __name__ == "__main__":
    main()




# n = int(input())
# plants = {}

# for i in range(n):
#     info = input().split("<->")
#     plant = info[0]
#     rarity = int(info[1])

#     if plant not in plants:
#         plants[plant] = {'rarity': rarity, 'ratings': []}

# while True:
#     command = input()
#     if command == 'Exhibition':
#         break
#     else:
#         tokens = command.split(": ")
#         action = tokens[0]

#         if action == 'Rate':
#             plant_information = tokens[1]
#             plant_info = plant_information.split(' - ')
#             plant_name = plant_info[0]
#             rating = int(plant_info[1])

#             if plant_name in plants:
#                 plants[plant_name]['ratings'].append(rating)
#             else:
#                 print("error")

#         elif action == 'Update':
#             update_information = tokens[1]
#             update_info = update_information.split(' - ')
#             plant_name = update_info[0]
#             new_rarity = int(update_info[1])

#             if plant_name in plants:
#                 plants[plant_name]['rarity'] = new_rarity
#             else:
#                 print("error")

#         elif action == 'Reset':
#             plant_name = tokens[1]

#             if plant_name in plants:
#                 plants[plant_name]['ratings'] = []
#             else:
#                 print("error")

# for plant, data in plants.items():
#     rarity = data['rarity']
#     ratings = data['ratings']

#     if ratings:
#         average_rating = sum(ratings) / len(ratings)
#     else:
#         average_rating = 0

#     plants[plant] = {'rarity': rarity, 'average_rating': average_rating}


# print("Plants for the exhibition:")
# for plant, data in plants.items():
#     rarity = data['rarity']
#     average_rating = data['average_rating']
#     print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
