def is_valid_index(lst, idx):
    return 0 <= idx < len(lst)


def memory_game():
    elements = input().split()
    moves = 0
    while True:
        command = input()
        if command == "end":
            break

        indices_data = command.split()
        index_1, index_2 = int(indices_data[0]), int(indices_data[1])
        moves += 1
        if is_valid_index(elements, index_1) and is_valid_index(elements, index_2) and index_1 != index_2:
            if elements[index_1] == elements[index_2]:
                matching_element = elements[index_1]
                while matching_element in elements:
                    elements.remove(matching_element)
                print(f"Congrats! You have found matching elements - {matching_element}!")

            else:
                print("Try again!")

        else:
            print("Invalid input! Adding additional elements to the board")
            index_middle_of_the_list = len(elements) // 2
            elements.insert(index_middle_of_the_list, f"-{moves}a")
            elements.insert(index_middle_of_the_list + 1, f"-{moves}a")

        if not elements:
            print(f"You have won in {moves} turns!")
            break

    if elements:
        print("Sorry you lose :(")
        print(*elements)


memory_game()





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


