n = int(input())
cars_data = {}

for i in range(n):
    car_info = input().split('|')
    car_brand, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])

    if car_brand not in cars_data:
        cars_data[car_brand] = {'mileage': mileage, 'fuel': fuel}

while True:
    command = input()
    if command == 'Stop':
        break

    info = command.split(' : ')
    if info[0] == "Drive":
        car_drive, distance, fuel_for_drive = info[1], int(info[2]), int(info[3])
        if car_drive in cars_data:
            if fuel_for_drive <= cars_data[car_drive]["fuel"]:
                print(f"{car_drive} driven for {distance} kilometers. {fuel_for_drive} liters of fuel consumed.")
                cars_data[car_drive]['mileage'] += distance
                cars_data[car_drive]['fuel'] -= fuel_for_drive
                if cars_data[car_drive]['mileage'] >= 100000:
                    del cars_data[car_drive]
                    print(f"Time to sell the {car_drive}!")
            else:
                print('Not enough fuel to make that ride')

    elif info[0] == 'Refuel':
        car_refuel, fuel_refuel = info[1], int(info[2])
        if cars_data[car_refuel]['fuel'] + fuel_refuel <= 75:
            cars_data[car_refuel]['fuel'] += fuel_refuel
            print(f"{car_refuel} refueled with {fuel_refuel} liters")
        else:
            diff_fuel = 75 - cars_data[car_refuel]['fuel']
            cars_data[car_refuel]['fuel'] = 75
            print(f"{car_refuel} refueled with {diff_fuel} liters")

    elif info[0] == 'Revert':
        car_revert, kilometers = info[1], int(info[2])

        if cars_data[car_revert]['mileage'] - kilometers >= 10000:
            cars_data[car_revert]['mileage'] -= kilometers
            print(f"{car_revert} mileage decreased by {kilometers} kilometers")
        else:
            cars_data[car_revert]['mileage'] = 10000

for curr_car, data in cars_data.items():
    total_mileage = data['mileage']
    fuel_left = data['fuel']
    print(f"{curr_car} -> Mileage: {total_mileage} kms, Fuel in the tank: {fuel_left} lt.")
