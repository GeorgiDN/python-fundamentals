elements = [i for i in input().split()]

moves = 0

while True:
    command = input()
    if command == "end":
        break

    [el_1, el_2] = command.split()
    el_1 = int(el_1)
    el_2 = int(el_2)
    moves += 1
    if el_1 == el_2 or el_1 not in range(len(elements)) or el_2 not in range(len(elements)):
        elements.insert(int(len(elements) // 2), f"-{moves}a")
        elements.insert(int(len(elements) // 2+1), f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    if elements[el_1] == elements[el_2]:
        print(f"Congrats! You have found matching elements - {elements[el_1]}!")
        elements = [el for el in elements if not el == elements[el_1] or not el == elements[el_2]]
    else:
        print("Try again!")
    if not elements:
        print(f"You have won in {moves} turns!")
        break

if len(elements) > 0:
    print("Sorry you lose :(")
    print(f"{' '.join(elements)}")





######################################################################################  CONDITION  ##########################################################################################################################################
# https://judge.softuni.org/Contests/Practice/Index/2517#2

# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. Until the player receives "end" from the console, you will receive strings with two integers separated by a space, representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence, you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a" 
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# •	On the first line, you will receive a sequence of elements.
# •	On the following lines, you will receive integers until the command "end".
# Output
# •	Every time the player hit two matching elements, you should remove them from the sequence and print on the console the following message:
# "Congrats! You have found matching elements - {element}!"
# •	If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# •	If the player hit all matching elements before he receives "end" from the console, you should print on the console the following message: 
# "You have won in {number of moves until now} turns!"
# •	If the player receives "end" before he hits all matching elements, you should print on the console the following message:
# "Sorry you lose :(
# {the current sequence's state}"
# Constraints
# •	All elements in the sequence will always have a matching element.


