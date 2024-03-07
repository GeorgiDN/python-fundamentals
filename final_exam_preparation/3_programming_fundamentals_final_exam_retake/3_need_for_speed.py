def take_initial_cars_data(cars_data_, num_of_cars):
    # [0 - MILEAGE, 1 - FUEL]
    for _ in range(num_of_cars):
        cars_info = input().split("|")
        curr_car, car_mileage, fuel_available = cars_info[0], int(cars_info[1]), int(cars_info[2])
        cars_data_[curr_car] = [car_mileage, fuel_available]
    return cars_data_


def drive(cars_data, car, distance, fuel):
    if fuel > cars_data[car][1]:
        print("Not enough fuel to make that ride")
    else:
        cars_data[car][0] += distance
        cars_data[car][1] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    if cars_data[car][0] >= 100000:
        del cars_data[car]
        print(f"Time to sell the {car}!")

    return cars_data


def refuel(cars_data, car, fuel, max_liters_of_fuel):
    if cars_data[car][1] + fuel <= max_liters_of_fuel:
        liters_to_refill = fuel
    else:
        liters_to_refill = max_liters_of_fuel - cars_data[car][1]
    cars_data[car][1] += liters_to_refill
    print(f"{car} refueled with {liters_to_refill} liters")
    return cars_data


def revert(cars_data, car, kilometers):
    if cars_data[car][0] - kilometers >= 10000:
        cars_data[car][0] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    else:
        cars_data[car][0] = 10000
    return cars_data


def print_result(cars_data):
    result = ''
    for vehicle, vehicle_data in cars_data.items():
        mileage_km, fuel_left = vehicle_data[0], vehicle_data[1]
        result += f"{vehicle} -> Mileage: {mileage_km} kms, Fuel in the tank: {fuel_left} lt.\n"
    return print(result)


def main():
    number_of_cars = int(input())
    cars_data = {}
    max_liters_of_fuel = 75

    cars_data = take_initial_cars_data(cars_data, number_of_cars)

    while True:
        command = input()
        if command == "Stop":
            break

        data = command.split(" : ")
        current_command = data[0]

        if current_command == "Drive":
            car, distance, fuel = data[1], int(data[2]), int(data[3])
            cars_data = drive(cars_data, car, distance, fuel)

        elif current_command == "Refuel":
            car, fuel = data[1], int(data[2])
            cars_data = refuel(cars_data, car,fuel, max_liters_of_fuel)

        elif current_command == "Revert":
            car, kilometers = data[1], int(data[2])
            cars_data = revert(cars_data, car, kilometers)

    print_result(cars_data)


if __name__ == "__main__":
    main()




# n = int(input())
# cars_data = {}

# for i in range(n):
#     car_info = input().split('|')
#     car_brand, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])

#     if car_brand not in cars_data:
#         cars_data[car_brand] = {'mileage': mileage, 'fuel': fuel}

# while True:
#     command = input()
#     if command == 'Stop':
#         break

#     info = command.split(' : ')
#     if info[0] == "Drive":
#         car_drive, distance, fuel_for_drive = info[1], int(info[2]), int(info[3])
#         if car_drive in cars_data:
#             if fuel_for_drive <= cars_data[car_drive]["fuel"]:
#                 print(f"{car_drive} driven for {distance} kilometers. {fuel_for_drive} liters of fuel consumed.")
#                 cars_data[car_drive]['mileage'] += distance
#                 cars_data[car_drive]['fuel'] -= fuel_for_drive
#                 if cars_data[car_drive]['mileage'] >= 100000:
#                     del cars_data[car_drive]
#                     print(f"Time to sell the {car_drive}!")
#             else:
#                 print('Not enough fuel to make that ride')

#     elif info[0] == 'Refuel':
#         car_refuel, fuel_refuel = info[1], int(info[2])
#         if cars_data[car_refuel]['fuel'] + fuel_refuel <= 75:
#             cars_data[car_refuel]['fuel'] += fuel_refuel
#             print(f"{car_refuel} refueled with {fuel_refuel} liters")
#         else:
#             diff_fuel = 75 - cars_data[car_refuel]['fuel']
#             cars_data[car_refuel]['fuel'] = 75
#             print(f"{car_refuel} refueled with {diff_fuel} liters")

#     elif info[0] == 'Revert':
#         car_revert, kilometers = info[1], int(info[2])

#         if cars_data[car_revert]['mileage'] - kilometers >= 10000:
#             cars_data[car_revert]['mileage'] -= kilometers
#             print(f"{car_revert} mileage decreased by {kilometers} kilometers")
#         else:
#             cars_data[car_revert]['mileage'] = 10000

# for curr_car, data in cars_data.items():
#     total_mileage = data['mileage']
#     fuel_left = data['fuel']
#     print(f"{curr_car} -> Mileage: {total_mileage} kms, Fuel in the tank: {fuel_left} lt.")
