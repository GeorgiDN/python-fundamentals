def register_in_contest(rankings, contest_and_passwords_info, curr_contest, curr_password, curr_username, curr_points):
    if curr_contest in contest_and_passwords_info and curr_password in contest_and_passwords_info[curr_contest]:
        if curr_username not in rankings:
            rankings[curr_username] = {}

        if curr_contest not in rankings[curr_username]:
            rankings[curr_username][curr_contest] = curr_points

        if curr_contest in rankings[curr_username]:
            if rankings[curr_username][curr_contest] < curr_points:
                rankings[curr_username][curr_contest] = curr_points

    return rankings


def sort_and_print_result(rankings):
    best_user = ""
    best_points = 0

    for user, user_submissions in rankings.items():
        total_points = sum(user_submissions.values())
        if total_points > best_points:
            best_user = user
            best_points = total_points

    print(f"Best candidate is {best_user} with total {best_points} points.")
    print("Ranking:")

    sorted_ranking_data = dict(sorted(rankings.items(), key=lambda x: x[0]))

    for user, user_submissions in sorted_ranking_data.items():
        print(user)
        sorted_contest_points = dict(sorted(user_submissions.items(), key=lambda x: -x[1]))
        for contest_, points_ in sorted_contest_points.items():
            print(f"#  {contest_} -> {points_}")


def ranking_task():
    contest_and_passwords_for_validate = {}
    ranking_data = {}
    end_of_contest = False
    while True:
        command = input()
        if not end_of_contest:
            if command == "end of contests":
                end_of_contest = True
                continue

            data = command.split(":")
            contest, password_for_contest = data[0], data[1]
            contest_and_passwords_for_validate[contest] = password_for_contest

        else:
            if command == "end of submissions":
                break

            data = command.split("=>")
            contest, password, username, points = data[0], data[1], data[2], int(data[3])
            ranking_data = \
                register_in_contest(ranking_data, contest_and_passwords_for_validate, contest, password, username, points)


    sort_and_print_result(ranking_data)


ranking_task()




# contests = {}
# submissions = {}

# while True:
#     command = input()
#     if command == "end of contests":
#         break
#     contest, password = command.split(":")
#     contests[contest] = password

# while True:
#     submission = input()
#     if submission == "end of submissions":
#         break
#     contest, password, username, points = submission.split("=>")
#     points = int(points)

#     if contest in contests and contests[contest] == password:
#         if username not in submissions:
#             submissions[username] = {}

#         if contest not in submissions[username]:
#             submissions[username][contest] = points
#         else:
#             if points > submissions[username][contest]:
#                 submissions[username][contest] = points

# best_user = ""
# best_points = 0

# for user, user_submissions in submissions.items():
#     total_points = sum(user_submissions.values())
#     if total_points > best_points:
#         best_user = user
#         best_points = total_points

# print(f"Best candidate is {best_user} with total {best_points} points.")
# print("Ranking:")
# sorted_submissions = dict(sorted(submissions.items(), key=lambda x: x[0]))

# for user, user_submissions in sorted_submissions.items():
#     print(user)
#     sorted_contests = dict(sorted(user_submissions.items(), key=lambda x: -x[1]))
#     for contest, points in sorted_contests.items():
#         print(f"#  {contest} -> {points}")
      
