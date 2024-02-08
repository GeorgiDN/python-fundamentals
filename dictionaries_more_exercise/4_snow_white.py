def snow_white():
    dwarfs_data = {}

    while True:
        line = input()
        if line == "Once upon a time":
            break

        dwarf_info = line.split(" <:> ")
        dwarf_name, dwarf_hat_color, dwarf_physics = dwarf_info[0], dwarf_info[1], int(dwarf_info[2])
        if dwarf_hat_color not in dwarfs_data:
            dwarfs_data[dwarf_hat_color] = {}
        else:
            if dwarf_name not in dwarfs_data[dwarf_hat_color]:
                dwarfs_data[dwarf_hat_color][dwarf_name] = 0
            else:
                if dwarf_physics < dwarfs_data[dwarf_hat_color][dwarf_name]:
                    dwarf_physics = dwarfs_data[dwarf_hat_color][dwarf_name]
        dwarfs_data[dwarf_hat_color][dwarf_name] = dwarf_physics

    dwarfs_dictionary = {}
    for hat_color, members in dwarfs_data.items():
        hat_length = len(members)
        for dwarf, physics in members.items():
            dwarf_name_color = f"{dwarf}|{hat_color}"
            dwarfs_dictionary[dwarf_name_color] = {"name": dwarf, "physics": physics, "members": hat_length,
                                             "hat_color": hat_color}

    sorted_dwarfs_dictionary = sorted(dwarfs_dictionary.items(), key=lambda x: (x[1]["physics"], x[1]['members']), reverse=True)
    for item in sorted_dwarfs_dictionary:
        current_dwarf = item[1]  # Access the second element of the tuple (index 1)
        print(f"({current_dwarf['hat_color']}) {current_dwarf['name']} <-> {current_dwarf['physics']}")

snow_white()
