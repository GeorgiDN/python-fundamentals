electrons = int(input())
shells = []
shell_number = 1

while electrons > 0:
    max_electrons_in_shell = 2 * shell_number ** 2
    if electrons >= max_electrons_in_shell:
        shells.append(max_electrons_in_shell)
    else:
        shells.append(electrons)
    electrons -= max_electrons_in_shell
    shell_number += 1

print(shells)
