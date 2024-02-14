def main():
    energy = int(input())
    out_of_energy = False
    won_battles = 0
    while True:
        command = input()
        if command == "End of battle":
            break

        distance = int(command)
        if energy >= distance:
            energy -= distance
            won_battles += 1
            if won_battles % 3 == 0:
                energy += won_battles
        else:
            print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
            out_of_energy = True
            break

    if not out_of_energy:
        print(f"Won battles: {won_battles}. Energy left: {energy}")


if __name__ == "__main__":
    main()





# def take_integer_input():
#     return int(input())


# def take_input():
#     return input()


# def print_not_enough_energy_message(won_battles_, energy_):
#     return print(f"Not enough energy! Game ends with {won_battles_} won battles and {energy_} energy")


# def print_won_battles_message(won_battles_, energy_):
#     return print(f"Won battles: {won_battles_}. Energy left: {energy_}")


# def battle_simulation():
#     won_battles = 0
#     energy = take_integer_input()
#     not_energy = False

#     while True:
#         command = take_input()
#         if command == "End of battle":
#             break

#         distance = int(command)
#         if energy - distance >= 0:
#             energy -= distance
#             won_battles += 1
#             if won_battles % 3 == 0:
#                 energy += won_battles
#         else:
#             not_energy = True
#             print_not_enough_energy_message(won_battles, energy)
#             break

#     if not not_energy:
#         print_won_battles_message(won_battles, energy)


# battle_simulation()




# won_battles = 0
# energy = int(input())
# not_energy = False

# while True:
#     command = input()
#     if command == "End of battle":
#         break

#     distance = int(command)
#     if energy - distance >= 0:
#         energy -= distance
#         won_battles += 1
#         if won_battles % 3 == 0:
#             energy += won_battles
#     else:
#         not_energy = True
#         print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
#         break

# if not not_energy:
#     print(f"Won battles: {won_battles}. Energy left: {energy}")



  
######################################################################################  CONDITION  ##########################################################################################################################################
#https://judge.softuni.org/Contests/Practice/Index/2305#0
# Write a program that keeps track of every won battle against an enemy. You will receive initial energy. Afterward, you will start receiving the distance you need to reach an enemy until the "End of battle" command is given, or you run out of energy.
# The energy you need for reaching an enemy is equal to the distance you receive. Each time you reach an enemy, you win a battle, and your energy is reduced. Otherwise, if you don't have enough energy to reach an enemy, end the program and print: "Not enough energy! Game ends with {count} won battles and {energy} energy".
# Every third won battle increases your energy with the value of your current count of won battles.
# Upon receiving the "End of battle" command, print the count of won battles in the following format:
# "Won battles: {count}. Energy left: {energy}" 
# Input / Constraints
# •	On the first line, you will receive initial energy – an integer [1-10000].
# •	On the following lines, you will be receiving the distance of an enemy – an integer [1-10000].
# Output
# •	The description contains the proper output messages for each case and the format they should be printed.
