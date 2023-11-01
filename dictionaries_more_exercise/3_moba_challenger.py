moba_players = {}
input_line = input().split()
while len(input_line) != 2:
    if input_line[1] == "->":
        name, position, skill = input_line[0], input_line[2], int(input_line[4])
        if name not in moba_players:
            moba_players[name] = {"total_skill": 0, position: 0}
        if position not in moba_players[name]:
            moba_players[name][position] = 0
        else:
            moba_players[name]["total_skill"] -= moba_players[name][position]
            if skill < moba_players[name][position]:
                skill = moba_players[name][position]
        moba_players[name][position] = skill
        moba_players[name]["total_skill"] += skill
    elif input_line[1] == "vs":
        player_one, player_two = input_line[0], input_line[2]
        common_positions = []
        positions_one = []
        positions_two = []
        for key_one, value_one in moba_players.items():
            if key_one == player_one:
                positions_one = list(x for x in moba_players[key_one].keys() if x != "total_skill")
                for key_two, value_two in moba_players.items():
                    if key_two == player_two:
                        positions_two = list(x for x in moba_players[key_two].keys() if x != "total_skill")
        for pos in positions_one:
            if pos in positions_two:
                common_positions.append(pos)
        if len(common_positions) > 0:
            if moba_players[player_one]["total_skill"] > moba_players[player_two]["total_skill"]:
                moba_players.pop(player_two)
            elif moba_players[player_one]["total_skill"] < moba_players[player_two]["total_skill"]:
                moba_players.pop(player_one)
    input_line = input().split()

sorted_players = sorted(moba_players, key=lambda x: (moba_players[x]["total_skill"]), reverse=True)
sorted_moba_players = {key: moba_players[key] for key in sorted_players}

for player, positions in sorted_moba_players.items():
    print(f"{player}: {positions['total_skill']} skill")
    sorted_positions = dict(sorted(positions.items(), key=lambda x: x[1], reverse=True))
    for key, value in sorted_positions.items():
        if key != "total_skill":
            print(f"- {key} <::> {value}")
          
