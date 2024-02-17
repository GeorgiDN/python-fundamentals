def validate_position(cupid_position_, neighborhood_):
    if not 0 <= cupid_position_ < len(neighborhood_):
        cupid_position_ = 0
    return cupid_position_


def cupid_jump_to_house(neighborhood_, cupid_position_):
    if neighborhood_[cupid_position_] == 0:
        print(f"Place {cupid_position_} already had Valentine's day.")
    else:
        neighborhood_[cupid_position_] -= 2
        if neighborhood_[cupid_position_] == 0:
            print(f"Place {cupid_position_} has Valentine's day.")
    return neighborhood_


def each_house_have_valentine_day(neighborhood_):
    return all(house == 0 for house in neighborhood_)


def houses_without_valentine_day(neighborhood_):
    return len([house for house in neighborhood_ if house > 0])


def main():
    neighborhood = list(map(int, input().split("@")))
    cupid_position = 0

    while True:
        command = input()
        if command == "Love!":
            break

        data = command.split()
        jump = int(data[1])

        cupid_position += jump
        cupid_position = validate_position(cupid_position, neighborhood)
        neighborhood = cupid_jump_to_house(neighborhood, cupid_position)

    print(f"Cupid's last position was {cupid_position}.")
    if each_house_have_valentine_day(neighborhood):
        print("Mission was successful.")
    else:
        houses_count = houses_without_valentine_day(neighborhood)
        print(f"Cupid has failed {houses_count} places.")


if __name__ == "__main__":
    main()



# def valid_index(lst, indx):
#     if 0 <= indx < len(lst):
#         return True
#     return None


# neighborhood = [int(x) for x in input().split('@')]
# cupid_position = 0

# while True:
#     command = input()
#     if command == 'Love!':
#         break

#     info = command.split(" ")
#     jump = int(info[1])
#     cupid_position += jump

#     if not valid_index(neighborhood, cupid_position):
#         cupid_position = 0
#     if neighborhood[cupid_position] == 0:
#         print(f"Place {cupid_position} already had Valentine's day.")
#         continue
#     neighborhood[cupid_position] -= 2
#     if neighborhood[cupid_position] == 0:
#         print(f"Place {cupid_position} has Valentine's day.")

# print(f"Cupid's last position was {cupid_position}.")

# # each_house_valentine_day = [house for house in neighborhood if house == 0]
# # if len(each_house_valentine_day) == len(neighborhood):
# if sum(neighborhood) == 0:
#     print("Mission was successful.")
# else:
#     failed_places = [house for house in neighborhood if house > 0]
#     print(f"Cupid has failed {len(failed_places)} places.")
  
