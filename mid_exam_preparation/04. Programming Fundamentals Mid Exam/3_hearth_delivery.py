def valid_index(lst, indx):
    if 0 <= indx < len(lst):
        return True
    return None


neighborhood = [int(x) for x in input().split('@')]
cupid_position = 0

while True:
    command = input()
    if command == 'Love!':
        break

    info = command.split(" ")
    jump = int(info[1])
    cupid_position += jump

    if not valid_index(neighborhood, cupid_position):
        cupid_position = 0
    if neighborhood[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")
        continue
    neighborhood[cupid_position] -= 2
    if neighborhood[cupid_position] == 0:
        print(f"Place {cupid_position} has Valentine's day.")

print(f"Cupid's last position was {cupid_position}.")

# each_house_valentine_day = [house for house in neighborhood if house == 0]
# if len(each_house_valentine_day) == len(neighborhood):
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    failed_places = [house for house in neighborhood if house > 0]
    print(f"Cupid has failed {len(failed_places)} places.")
  
