my_car_list = list(map(int, input().split()))

half_size = len(my_car_list) // 2

left_side_cars_time = 0
right_side_cars_time = 0

left_half = my_car_list[:half_size]
right_half = my_car_list[1 + half_size:]

for i in left_half:
    if i != 0:
        left_side_cars_time += i
    elif i == 0:
        left_side_cars_time *= 0.8

for j in reversed(right_half):
    if j != 0:
        right_side_cars_time += j
    elif j == 0:
        right_side_cars_time *= 0.8

if left_side_cars_time < right_side_cars_time:
    print(f'The winner is left with total time: {left_side_cars_time:.1f}')

elif left_side_cars_time > right_side_cars_time:
    print(f'The winner is right with total time: {right_side_cars_time:.1f}')
