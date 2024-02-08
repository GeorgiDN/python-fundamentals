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




####################################
# def sort_and_print_result(contests_info, standings):
#     sorted_contestants = list(contests_info.items())
#     for curr_contest, participants in sorted_contestants:
#         print(f"{curr_contest}: {len(participants)} participants")
#         sorted_participants = dict(sorted(participants.items(), key=lambda x: (-x[1], x[0])))
#         for idx, (username, curr_points) in enumerate(sorted_participants.items(), start=1):
#             print(f"{idx}. {username} <::> {curr_points}")
#
#     print("Individual standings:")
#     sorted_individual_points = dict(sorted(standings.items(), key=lambda x: (-x[1], x[0])))
#     for idx, (username, total_points) in enumerate(sorted_individual_points.items(), start=1):
#         print(f"{idx}. {username} -> {total_points}")
#
#
# def judge_task():
#     contests_data = {}
#     individual_standings = {}
#     while True:
#         command = input()
#         if command == "no more time":
#             break
#
#         data = command.split(" -> ")
#         name, contest, points = data[0], data[1], int(data[2],)
#
#         if contest not in contests_data:
#             contests_data[contest] = {}
#
#         if name not in contests_data[contest]:
#             contests_data[contest][name] = points
#             if name not in individual_standings:
#                 individual_standings[name] = 0
#             individual_standings[name] += points
#
#         else:
#             if contests_data[contest][name] < points:
#                 contests_data[contest][name] = points
#                 individual_standings[name] = points
#
#     sort_and_print_result(contests_data, individual_standings)
#
#
# judge_task()



####################################
# contests_data = {}
# individual_standings = {}
# 
# while True:
#     command = input()
# 
#     if command == "no more time":
#         break
# 
#     name, contest, points = command.split(" -> ")
#     points = int(points)
# 
#     if contest not in contests_data:
#         contests_data[contest] = {}
# 
#     if name not in contests_data[contest]:
#         contests_data[contest][name] = points
#         if name not in individual_standings:
#             individual_standings[name] = 0
#         individual_standings[name] += points
# 
#     else:
#         if contests_data[contest][name] < points:
#             contests_data[contest][name] = points
#             individual_standings[name] = points
# 
# sorted_contestants = list(contests_data.items())
# 
# for contest, participants in sorted_contestants:
#     print(f"{contest}: {len(participants)} participants")
#     sorted_participants = dict(sorted(participants.items(), key=lambda x: (-x[1], x[0])))
#     for idx, (username, points) in enumerate(sorted_participants.items(), start=1):
#         print(f"{idx}. {username} <::> {points}")
# 
# print("Individual standings:")
# sorted_individual_points = dict(sorted(individual_standings.items(), key=lambda x: (-x[1], x[0])))
# for idx, (username, total_points) in enumerate(sorted_individual_points.items(), start=1):
#     print(f"{idx}. {username} -> {total_points}")




########################
# contests = {}
# users_standings = {}
# line = input().split(" -> ")
#
# while line[0] != "no more time":
#     username, contest, points = line[0], line[1], int(line[2])
#     if contest not in contests:
#         contests[contest] = {username: 0}
#     if username not in contests[contest]:
#         contests[contest][username] = 0
#     else:
#         if points < contests[contest][username]:
#             points = contests[contest][username]
#     contests[contest][username] = points
#     contests[contest][username] = points
#     if username not in users_standings:
#         users_standings[username] = {"total_points": 0, contest: 0}
#     if contest not in users_standings[username]:
#         users_standings[username][contest] = 0
#     else:
#         users_standings[username]["total_points"] -= users_standings[username][contest]
#         if points < users_standings[username][contest]:
#             points = users_standings[username][contest]
#     users_standings[username]["total_points"] += points
#     users_standings[username][contest] = points
#     line = input().split(" -> ")
#
# for contest in contests:
#     print(f"{contest}: {len(contests[contest])} participants")
#     sorted_participants = sorted(contests[contest].items(), key=lambda x: (-x[1], x[0]))
#     sorted_contest = dict(sorted_participants)
#     counter = 0
#     for participant, points in sorted_contest.items():
#         counter += 1
#         print(f"{counter}. {participant} <::> {points}")
#
# new_keys = []
# new_values = []
# for key, value in users_standings.items():
#     new_keys.append(key)
#     new_values.append(value["total_points"])
# user_scores = dict(zip(new_keys, new_values))
# sorted_scores = dict(sorted(user_scores.items(), key=lambda k: (-k[1], k[0])))
# print("Individual standings:")
# counter = 0
# for name, curr_points in sorted_scores.items():
#     counter += 1
#     print(f"{counter}. {name} -> {curr_points}")
