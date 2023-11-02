dwarfs = {}
input_line = input()
while input_line != "Once upon a time":
    dwarf_info = input_line.split(" <:> ")
    dwarf_name, dwarf_hat_color, dwarf_physics = dwarf_info[0], dwarf_info[1], int(dwarf_info[2])
    if dwarf_hat_color not in dwarfs:
        dwarfs[dwarf_hat_color] = {}
    else:
        if dwarf_name not in dwarfs[dwarf_hat_color]:
            dwarfs[dwarf_hat_color][dwarf_name] = 0
        else:
            if dwarf_physics < dwarfs[dwarf_hat_color][dwarf_name]:
                dwarf_physics = dwarfs[dwarf_hat_color][dwarf_name]
    dwarfs[dwarf_hat_color][dwarf_name] = dwarf_physics
    input_line = input()

dwarfs_dict = {}
for hat_color, members in dwarfs.items():
    hat_length = len(members)
    for dwarf, physics in members.items():
        dwarf_name_color = f"{dwarf}|{hat_color}"
        dwarfs_dict[dwarf_name_color] = {"name": dwarf, "physics": physics, "members": hat_length,
                                         "hat_color": hat_color}

for item in sorted(dwarfs_dict, key=lambda k: (dwarfs_dict[k]['physics'], dwarfs_dict[k]['members']), reverse=True):
    current_dwarf = dwarfs_dict[item]
    print(f"({current_dwarf['hat_color']}) {current_dwarf['name']} <-> {current_dwarf['physics']}")
