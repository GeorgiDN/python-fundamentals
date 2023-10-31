sides = {}
users = []
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side = command.split(" | ")[0]
        force_user = command.split(" | ")[1]
        if force_user not in users:
            users.append(force_user)
            if force_side not in sides:
                sides[force_side] = []
            sides[force_side].append(force_user)
    elif "->" in command:
        force_side = command.split(" -> ")[1]
        force_user = command.split(" -> ")[0]
        if force_user in users:
            if force_side not in sides:
                sides[force_side] = []
            sides[force_side].append(force_user)
            for key, value in sides.items():
                if key != force_side and force_user in value:
                    sides[key].remove(force_user)
        else:
            users.append(force_user)
            if force_side not in sides:
                sides[force_side] = []
            sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_sides, force_users in sides.items():
    if len(force_users) > 0:
        print(f"Side: {force_sides}, Members: {len(force_users)}")
        for member in force_users:
            print(f"! {member}")
          
