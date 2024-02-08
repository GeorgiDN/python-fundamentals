def sort_and_print_result(contests, standings):
    for curr_contest, participants in contests.items():
        print(f"{curr_contest}: {len(participants)} participants")
        sorted_contest_data = dict(sorted(participants.items(), key=lambda x: (-x[1], x[0])))
        num = 1
        for user, curr_points in sorted_contest_data.items():
            print(f"{num}. {user} <::> {curr_points}")
            num += 1

    sorted_individual_standings = dict(sorted(standings.items(), key=lambda x: (-x[1], x[0])))
    num = 1
    print("Individual standings:")
    for curr_name, current_points in sorted_individual_standings.items():
        print(f"{num}. {curr_name} -> {current_points}")
        num += 1


def judge_task():
    contests_data = {}
    individual_standings = {}
    while True:
        command = input()
        if command == "no more time":
            break

        data = command.split(" -> ")
        name, contest, points = data[0], data[1], int(data[2],)

        if contest not in contests_data:
            contests_data[contest] = {}

        if name not in contests_data[contest]:
            contests_data[contest][name] = points
            if name not in individual_standings:
                individual_standings[name] = 0
            individual_standings[name] += points

        else:
            if contests_data[contest][name] < points:
                contests_data[contest][name] = points
                individual_standings[name] = points

    sort_and_print_result(contests_data, individual_standings)


judge_task()
  
