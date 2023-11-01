users = {}
contests = {}
input_line = input().split(" -> ")
while input_line[0] != "no more time":
    username, contest, points = input_line[0], input_line[1], int(input_line[2])
    if contest not in contests:
        contests[contest] = {username: 0}
    if username not in contests[contest]:
        contests[contest][username] = 0
    else:
        if points < contests[contest][username]:
            points = contests[contest][username]
    contests[contest][username] = points
    contests[contest][username] = points
    if username not in users:
        users[username] = {"total_points": 0, contest: 0}
    if contest not in users[username]:
        users[username][contest] = 0
    else:
        users[username]["total_points"] -= users[username][contest]
        if points < users[username][contest]:
            points = users[username][contest]
    users[username]["total_points"] += points
    users[username][contest] = points
    input_line = input().split(" -> ")

for contest in contests:
    print(f"{contest}: {len(contests[contest])} participants")
    sorted_participants = sorted(contests[contest].items(), key=lambda x: (-x[1], x[0]))
    sorted_contest = dict(sorted_participants)
    counter = 0
    for participant, points in sorted_contest.items():
        counter += 1
        print(f"{counter}. {participant} <::> {points}")

new_keys = []
new_values = []
for key, value in users.items():
    new_keys.append(key)
    new_values.append(value["total_points"])
user_scores = dict(zip(new_keys, new_values))
sorted_scores = dict(sorted(user_scores.items(), key=lambda k: (-k[1], k[0])))
print("Individual standings:")
counter = 0
for key, value in sorted_scores.items():
    counter += 1
    print(f"{counter}. {key} -> {value}")
  
