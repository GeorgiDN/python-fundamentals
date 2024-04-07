animal_data = {}

while True:
    command = input()
    if command == "EndDay":
        break

    data = command.replace(": ", "-")
    data = data.split("-")
    command = data[0]
    name = data[1]

    if command == "Add":
        need_food, area = int(data[2]), data[3]
        if name not in animal_data:
            animal_data[name] = []  # 0 food, 1 area
            animal_data[name].append(need_food)
            animal_data[name].append(area)
        else:
            animal_data[name][0] += need_food

    elif command == "Feed":
        food = int(data[2])
        if name in animal_data:
            animal_data[name][0] -= food

            if animal_data[name][0] <= 0:
                print(f"{name} was successfully fed")
                del animal_data[name]

hungry_animals = {}
print("Animals:")
for animal, data in animal_data.items():
    food_quantity, curr_area = int(data[0]), data[1]
    if curr_area not in hungry_animals:
        hungry_animals[curr_area] = 0
    hungry_animals[curr_area] += 1
    print(f" {animal} -> {food_quantity}g")

print("Areas with hungry animals:")
for ar, num in hungry_animals.items():
    print(f" {ar}: {num}")
