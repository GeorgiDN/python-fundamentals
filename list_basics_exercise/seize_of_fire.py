valid_types_of_fire = {"High": range(81, 126), "Medium": range(51, 81), "Low": range(1, 51)}

cells_with_fire = [x for x in input().split("#")]
quantity_of_water = int(input())
total_fire = 0
total_effort = 0
extinguished_cells = []

for i in range(len(cells_with_fire)):
    if quantity_of_water == 0:
        break
    info = cells_with_fire[i].split(" = ")
    fire_type, fire_value_of_cell = info[0], int(info[1])
    if quantity_of_water - fire_value_of_cell >= 0:
        if fire_value_of_cell in valid_types_of_fire[fire_type]:
            quantity_of_water -= fire_value_of_cell
            total_fire += fire_value_of_cell
            twenty_five_percent_of_cell_value = fire_value_of_cell * 0.25
            total_effort += twenty_five_percent_of_cell_value
            extinguished_cells.append(fire_value_of_cell)

print("Cells:")
if extinguished_cells:
    for cell in extinguished_cells:
        print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")



# fires = input().split("#")
# water = int(input())

# total_fire = 0
# effort = 0
# extinguished_cells = []

# for fire in fires:
#     fire_info = fire.split(" = ")
#     fire_type = fire_info[0]
#     fire_value = int(fire_info[1])

#     valid_ranges = {"High": range(81, 126), "Medium": range(51, 81), "Low": range(1, 51)}

#     if fire_value in valid_ranges[fire_type]:
#         if water >= fire_value:
#             extinguished_cells.append(fire_value)
#             water -= fire_value
#             total_fire += fire_value
#             effort += fire_value * 0.25

# print("Cells:")
# for cell in extinguished_cells:
#     print(f"- {cell}")

# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")
