def valid_index(lst, indx):
    if 0 <= indx < len(lst):
        return True
    return None


targets = list(map(int, input().split(' ')))
shot_indices = []

while True:
    command = input()
    if command == 'End':
        break

    idx = int(command)
    if valid_index(targets, idx) and idx not in shot_indices:
        value_ = targets[idx]
        targets.pop(idx)

        for i, val in enumerate(targets):
            if val >= 0:
                if val > value_:
                    targets[i] -= value_
                else:
                    targets[i] += value_

        targets.insert(idx, -1)
        shot_indices.append(idx)

print(f"Shot targets: {len(shot_indices)} -> {' '.join(map(str, targets))}")


######################################################################################  CONDITION  ##########################################################################################################################################
#https://judge.softuni.org/Contests/Practice/Index/2305#1
# Write a program that helps you keep track of your shot targets. You will receive a sequence with integers, separated by a single space, representing targets and their value. Afterward, you will be receiving indices until the "End" command is given, and you need to print the targets and the count of shot targets.
# Every time you receive an index, you need to shoot the target on that index, if it is possible. 
# Every time you shoot a target, its value becomes -1, and it is considered a shot. Along with that, you also need to:
# •	Reduce all the other targets, which have greater values than your current target, with its value. 
# •	Increase all the other targets, which have less than or equal value to the shot target, with its value.
# Keep in mind that you can't shoot a target, which is already shot. You also can't increase or reduce a target, which is considered a shot.
# When you receive the "End" command, print the targets in their current state and the count of shot targets in the following format:
# "Shot targets: {count} -> {target1} {target2}… {targetn}"
# Input / Constraints
# •	On the first line of input, you will receive a sequence of integers, separated by a single space – the targets sequence.
# •	On the following lines, until the "End" command, you be receiving integers each on a single line – the index of the target to be shot.
# Output
# •	The format of the output is described above in the problem description.
