contests = {}
submissions = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    contests[contest] = password

while True:
    submission = input()
    if submission == "end of submissions":
        break
    contest, password, username, points = submission.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in submissions:
            submissions[username] = {}

        if contest not in submissions[username]:
            submissions[username][contest] = points
        else:
            if points > submissions[username][contest]:
                submissions[username][contest] = points

best_user = ""
best_points = 0

for user, user_submissions in submissions.items():
    total_points = sum(user_submissions.values())
    if total_points > best_points:
        best_user = user
        best_points = total_points

print(f"Best candidate is {best_user} with total {best_points} points.")
print("Ranking:")
sorted_submissions = dict(sorted(submissions.items(), key=lambda x: x[0]))

for user, user_submissions in sorted_submissions.items():
    print(user)
    sorted_contests = dict(sorted(user_submissions.items(), key=lambda x: -x[1]))
    for contest, points in sorted_contests.items():
        print(f"#  {contest} -> {points}")
      
