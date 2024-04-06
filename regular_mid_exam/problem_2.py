valid_car_types = ["family", "heavyDuty", "sports"]
invalid_message = "Invalid car type."

total_taxes = 0

cars_data = input().split(">>")
for car in cars_data:
    info = car.split()
    car_type, years, kilometres = info[0], int(info[1]), int(info[2])

    if car_type == "family":
        increased_by = kilometres // 3000
        family_car_taxes = increased_by * 12 + (50 - years * 5)
        total_taxes += family_car_taxes
        print(f"A {car_type} car will pay {family_car_taxes:.2f} euros in taxes.")

    elif car_type == "heavyDuty":
        increased_by = kilometres // 9000
        heavy_duty = increased_by * 14 + (80 - years * 8)
        total_taxes += heavy_duty
        print(f"A {car_type} car will pay {heavy_duty:.2f} euros in taxes.")

    elif car_type == "sports":
        increased_by = kilometres // 2000
        sports_car = increased_by * 18 + (100 - years * 9)
        total_taxes += sports_car
        print(f"A {car_type} car will pay {sports_car:.2f} euros in taxes.")
    else:
        print(invalid_message)

print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")
