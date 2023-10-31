exam_results = {}
banned = []
command = input()
while command != "exam finished":
    current_submission = command.split("-")
    if len(current_submission) == 2:
        current_username = current_submission[0]
        banned.append(current_username)
    else:
        current_username, current_language = current_submission[0], current_submission[1]
        current_points = int(current_submission[2])
        if current_language not in exam_results:
            exam_results[current_language] = {"submissions": 0}
        if current_username in exam_results[current_language]:
            if exam_results[current_language][current_username] > current_points:
                current_points = exam_results[current_language][current_username]
        exam_results[current_language][current_username] = current_points
        exam_results[current_language]["submissions"] += 1
    command = input()
print("Results:")
for value in exam_results.values():
    for person, points in value.items():
        if person not in banned and person != "submissions":
            print(f"{person} | {points}")
print("Submissions:")
for value, key in exam_results.items():
    print(f"{value} - {exam_results[value]['submissions']}")
