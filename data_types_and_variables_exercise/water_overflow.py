follow_number = int(input())
capacity = 255
liters_in_tank = 0

for pour in range(follow_number):
    liters = int(input())
    liters_in_tank += liters
    if capacity < liters_in_tank:
        liters_in_tank -= liters
        print('Insufficient capacity!')

print(liters_in_tank)
