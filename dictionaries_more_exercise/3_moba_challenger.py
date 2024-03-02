def duel_starts(moba_players_data, player_one, player_two):
    common_positions = []
    positions_one = []
    positions_two = []
    for key_one, value_one in moba_players_data.items():
        if key_one == player_one:
            positions_one = list(x for x in moba_players_data[key_one].keys() if x != "total_skill")
            for key_two, value_two in moba_players_data.items():
                if key_two == player_two:
                    positions_two = list(x for x in moba_players_data[key_two].keys() if x != "total_skill")

    for curr_position in positions_one:
        if curr_position in positions_two:
            common_positions.append(curr_position)
    if len(common_positions) > 0:
        if moba_players_data[player_one]["total_skill"] > moba_players_data[player_two]["total_skill"]:
            moba_players_data.pop(player_two)
        elif moba_players_data[player_one]["total_skill"] < moba_players_data[player_two]["total_skill"]:
            moba_players_data.pop(player_one)

    return moba_players_data


def print_result(sorted_moba_players):
    for player, positions in sorted_moba_players.items():
        print(f"{player}: {positions['total_skill']} skill")
        sorted_positions = dict(sorted(positions.items(), key=lambda x: x[1], reverse=True))
        for key, value in sorted_positions.items():
            if key != "total_skill":
                print(f"- {key} <::> {value}")


def take_info(moba_players_data, name, position, skill):
    if name not in moba_players_data:
        moba_players_data[name] = {"total_skill": 0, position: 0}

    if position not in moba_players_data[name]:
        moba_players_data[name][position] = 0
    else:
        moba_players_data[name]["total_skill"] -= moba_players_data[name][position]
        if skill < moba_players_data[name][position]:
            skill = moba_players_data[name][position]
    moba_players_data[name][position] = skill
    moba_players_data[name]["total_skill"] += skill

    return moba_players_data


def main():
    moba_players_data = {}
    while True:
        players_info = input().split()
        if len(players_info) == 2:
            break
        if players_info[1] == "->":
            name, position, skill = players_info[0], players_info[2], int(players_info[4])

            moba_players_data = take_info(moba_players_data, name, position, skill)

        elif players_info[1] == "vs":
            player_one, player_two = players_info[0], players_info[2]
            moba_players_data = duel_starts(moba_players_data, player_one, player_two)

    sorted_players = sorted(moba_players_data, key=lambda x: (moba_players_data[x]["total_skill"]), reverse=True)
    sorted_moba_players = {key: moba_players_data[key] for key in sorted_players}

    print_result(sorted_moba_players)


if __name__ == "__main__":
    main()
