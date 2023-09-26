fires = input().split("#")
water = int(input())

total_fire = 0
effort = 0
extinguished_cells = []

for fire in fires:
    fire_info = fire.split(" = ")
    fire_type = fire_info[0]
    fire_value = int(fire_info[1])

    valid_ranges = {"High": range(81, 126), "Medium": range(51, 81), "Low": range(1, 51)}

    if fire_value in valid_ranges[fire_type]:
        if water >= fire_value:
            extinguished_cells.append(fire_value)
            water -= fire_value
            total_fire += fire_value
            effort += fire_value * 0.25

print("Cells:")
for cell in extinguished_cells:
    print(f"- {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
