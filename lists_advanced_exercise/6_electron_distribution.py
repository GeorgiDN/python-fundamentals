shells = []
for n in range(1, number_of_electrons + 1):
    shell = 2 * n ** 2
    if number_of_electrons - shell >= 0:
        number_of_electrons -= shell
        shells.append(shell)
    else:
        shells.append(number_of_electrons)
        break

print(shells)



# electrons = int(input())
# shells = []
# shell_number = 1

# while electrons > 0:
#     max_electrons_in_shell = 2 * shell_number ** 2
#     if electrons >= max_electrons_in_shell:
#         shells.append(max_electrons_in_shell)
#     else:
#         shells.append(electrons)
#     electrons -= max_electrons_in_shell
#     shell_number += 1

# print(shells)
