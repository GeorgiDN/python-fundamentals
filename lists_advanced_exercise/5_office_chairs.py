rooms = int(input())
game_on = True

free_chairs = 0
for room in range(1, rooms + 1):
    chairs, visitors = input().split(" ")
    number_chairs = len(chairs)
    number_visitors = int(visitors)

    difference = abs(number_visitors - number_chairs)

    if number_chairs > number_visitors:
        free_chairs += difference

    elif number_chairs < number_visitors:
        game_on = False
        print(f"{difference} more chairs needed in room {room}")

if game_on:
    print(f"Game On, {free_chairs} free chairs left")




# rooms = int(input())

# chairs_left = 0
# enough_chairs = True

# for room in range(1, rooms + 1):
#     info = input().split()
#     chairs = len(info[0])
#     visitor = int(info[1])
#     if chairs < visitor:
#         enough_chairs = False
#         print(f"{visitor - chairs} more chairs needed in room {room}")
#     else:
#         chairs_left += abs(chairs - visitor)

# if enough_chairs:
#     print(f"Game On, {chairs_left} free chairs left")
