rooms = int(input())

chairs_left = 0
enough_chairs = True

for room in range(1, rooms + 1):
    info = input().split()
    chairs = len(info[0])
    visitor = int(info[1])
    if chairs < visitor:
        enough_chairs = False
        print(f"{visitor - chairs} more chairs needed in room {room}")
    else:
        chairs_left += abs(chairs - visitor)

if enough_chairs:
    print(f"Game On, {chairs_left} free chairs left")
