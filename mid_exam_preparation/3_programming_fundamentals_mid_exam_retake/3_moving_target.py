def is_valid(targets_, shoot_index_):
    return 0 <= shoot_index_ < len(targets_)


def shoot(targets_, shoot_index_, power_):
    if is_valid(targets_, shoot_index_):
        targets_[shoot_index_] -= power_
        if targets_[shoot_index_] <= 0:
            if len(targets_) > 1:
                targets_.pop(shoot_index_)
            else:
                target = targets_.index(shoot_index_)
                targets_.remove(target)

    return targets_


def add(targets_, add_index_, value_):
    if is_valid(targets_, add_index_):
        targets_.insert(add_index_, value_)
    else:
        print("Invalid placement!")

    return targets_


def strike(targets_, strike_index_, radius_):
    if is_valid(targets_, strike_index_ - radius_) and is_valid(targets_, strike_index_ + radius_):
        targets_ = targets_[:strike_index_ - radius_] + targets_[strike_index_ + radius_ + 1:]
    else:
        print("Strike missed!")

    return targets_


def moving_target():
    targets = list(map(int, input().split()))
    while True:
        command = input()
        if command == "End":
            break

        data = command.split()
        current_command = data[0]

        if current_command == "Shoot":
            shoot_index, power = int(data[1]), int(data[2])
            targets = shoot(targets, shoot_index, power)

        elif current_command == "Add":
            add_index, value = int(data[1]), int(data[2])
            targets = add(targets, add_index, value)

        elif current_command == "Strike":
            strike_index, radius = int(data[1]), int(data[2])
            targets = strike(targets, strike_index, radius)

    if targets:
        print("|".join(map(str, targets)))


moving_target()



##################################################################################################
# def valid_index(lst, indx):
#     return 0 <= indx < len(lst)
# 
# 
# def valid_radius(targets, index, r):
#     return 0 <= index - r < len(targets) and index + r < len(targets)
# 
# 
# def shoot(targets, shoot_idx, power):
#     if valid_index(targets, shoot_idx):
#         targets[shoot_idx] -= power
#         if targets[shoot_idx] <= 0:
#             targets.pop(shoot_idx)
#     return targets
# 
# 
# def add(targets, add_idx, add_value):
#     if valid_index(targets, add_idx):
#         targets.insert(add_idx, add_value)
#     else:
#         print("Invalid placement!")
#     return targets
# 
# 
# def strike(targets, strike_idx, radius):
#     if valid_radius(targets, strike_idx, radius):
#         start = max(0, strike_idx - radius)
#         end = min(len(targets), strike_idx + radius + 1)
#         del targets[start:end]
#     else:
#         print("Strike missed!")
#     return targets
# 
# 
# def main():
#     target_sequence = [int(x) for x in input().split(' ')]
# 
#     while True:
#         command = input()
#         if command == 'End':
#             break
# 
#         info = command.split(" ")
#         action = info[0]
# 
#         if action == "Shoot":
#             shoot_idx, power = int(info[1]), int(info[2])
#             target_sequence = shoot(target_sequence, shoot_idx, power)
# 
#         elif action == "Add":
#             add_idx, add_value = int(info[1]), int(info[2])
#             target_sequence = add(target_sequence, add_idx, add_value)
# 
#         elif action == "Strike":
#             strike_idx, radius = int(info[1]), int(info[2])
#             target_sequence = strike(target_sequence, strike_idx, radius)
# 
#     print('|'.join(map(str, target_sequence)))
# 
# 
# if __name__ == "__main__":
#     main()



########################################################################################
# def valid_index(lst, indx):
#     if 0 <= indx < len(lst):
#         return True
#     return None
# 
# 
# def valid_radius(targets, index, r):
#     if 0 <= index - r < len(targets) and index + r < len(targets):
#         return True
#     return None
# 
# 
# target_sequence = [int(x) for x in input().split(' ')]
# 
# while True:
#     command = input()
#     if command == 'End':
#         break
# 
#     info = command.split(" ")
#     action = info[0]
# 
#     if action == "Shoot":
#         shoot_idx, power = int(info[1]), int(info[2])
#         if valid_index(target_sequence, shoot_idx):
#             target_sequence[shoot_idx] -= power
#             if target_sequence[shoot_idx] <= 0:
#                 target_sequence.pop(shoot_idx)
# 
#     elif action == "Add":
#         add_idx, add_value = int(info[1]), int(info[2])
#         if valid_index(target_sequence, add_idx):
#             target_sequence.insert(add_idx, add_value)
#         else:
#             print("Invalid placement!")
# 
#     elif action == "Strike":
#         strike_idx, radius = int(info[1]), int(info[2])
#         if valid_radius(target_sequence, strike_idx, radius):
#             for i in range(radius+2):
#                 target_sequence.pop(strike_idx-1)
# 
#         else:
#             print("Strike missed!")
# 
# print('|'.join(map(str, target_sequence)))




#############################################################################################
# def valid_index(lst, indx):
#     if 0 <= indx < len(lst):
#         return True
#     return None
# 
# 
# def valid_radius(targets, index, r):
#     if 0 <= index - r < len(targets) and index + r < len(targets):
#         return True
#     return None
# 
# 
# target_sequence = [int(x) for x in input().split(' ')]
# 
# while True:
#     command = input()
#     if command == 'End':
#         break
# 
#     info = command.split(" ")
#     action = info[0]
# 
#     if action == "Shoot":
#         shoot_idx, power = int(info[1]), int(info[2])
#         if valid_index(target_sequence, shoot_idx):
#             target_sequence[shoot_idx] -= power
#             if target_sequence[shoot_idx] <= 0:
#                 target_sequence.pop(shoot_idx)
# 
#     elif action == "Add":
#         add_idx, add_value = int(info[1]), int(info[2])
#         if valid_index(target_sequence, add_idx):
#             target_sequence.insert(add_idx, add_value)
#         else:
#             print("Invalid placement!")
# 
#     elif action == "Strike":
#         strike_idx, radius = int(info[1]), int(info[2])
#         if valid_radius(target_sequence, strike_idx, radius):
#             start_idx = max(0, strike_idx - radius)
#             end_idx = min(len(target_sequence), strike_idx + radius + 1)
#             target_sequence = target_sequence[:start_idx] + target_sequence[end_idx:]
#         else:
#             print("Strike missed!")
# 
# print('|'.join(map(str, target_sequence)))





######################################################################################  CONDITION  ##########################################################################################################################################
# https://judge.softuni.org/Contests/Practice/Index/2305#2
# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the first line, you will receive a sequence of targets with their integer values, split by a single space. Then, you will start receiving commands for manipulating the targets until the "End" command. The commands are the following:
# •	"Shoot {index} {power}"
# o	Shoot the target at the index if it exists by reducing its value by the given power (integer value). 
# o	Remove the target if it is shot. A target is considered shot when its value reaches 0.
# •	"Add {index} {value}"
# o	Insert a target with the received value at the received index if it exists. 
# o	If not, print: "Invalid placement!"
# •	"Strike {index} {radius}"
# o	Remove the target at the given index and the ones before and after it depending on the radius.
# o	If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
#  Example:  "Strike 2 2"
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}		

# •	"End"
# o	Print the sequence with targets in the following format and end the program:
# "{target1}|{target2}…|{targetn}"
# Input / Constraints
# •	On the first line, you will receive the sequence of targets – integer values [1-10000].
# •	On the following lines, until the "End" will be receiving the command described above – strings.
# •	There will never be a case when the "Strike" command would empty the whole sequence.
# Output
# •	Print the appropriate message in case of any command if necessary.
# •	In the end, print the sequence of targets in the format described above.




