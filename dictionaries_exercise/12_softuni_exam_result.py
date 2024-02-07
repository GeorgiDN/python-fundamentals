def ban(curr_name, results):
    if curr_name in results:
        del results[curr_name]
    return results


def take_the_result(results, submissions, curr_name, curr_language, curr_points):
    if curr_name not in results:
        results[curr_name] = {}
        results[curr_name]["languages"] = curr_language
        results[curr_name]["points"] = curr_points
        results[curr_name]["points"] = curr_points

    elif curr_language not in results[curr_name]["languages"]:
        results[curr_name]["languages"] = curr_language
        results[curr_name]["points"] = curr_points

    else:
        if curr_language in results[curr_name]["languages"]:
            if curr_points > results[curr_name]["points"]:
                results[curr_name]["points"] = curr_points

    if curr_language not in submissions:
        submissions[curr_language] = 0
    submissions[curr_language] += 1

    return results, submissions


def softuni_exam_result():
    results_contests = {}
    submissions_data = {}
    while True:
        command = input()
        if command == "exam finished":
            break

        data = command.split("-")
        if data[1] == "banned":
            name = data[0]
            results_contests = ban(name, results_contests)

        else:
            name, language, points = data[0], data[1], int(data[2])
            results_contests, submissions_data = \
                take_the_result(results_contests, submissions_data, name, language, points)

    print("Results:")
    for name_, data_ in results_contests.items():
        print(f"{name_} | {data_['points']}")

    print("Submissions:")
    for lang, num in submissions_data.items():
        print(f"{lang} - {num}")


softuni_exam_result()



# exam_results = {}
# banned = []
# command = input()
# while command != "exam finished":
#     current_submission = command.split("-")
#     if len(current_submission) == 2:
#         current_username = current_submission[0]
#         banned.append(current_username)
#     else:
#         current_username, current_language = current_submission[0], current_submission[1]
#         current_points = int(current_submission[2])
#         if current_language not in exam_results:
#             exam_results[current_language] = {"submissions": 0}
#         if current_username in exam_results[current_language]:
#             if exam_results[current_language][current_username] > current_points:
#                 current_points = exam_results[current_language][current_username]
#         exam_results[current_language][current_username] = current_points
#         exam_results[current_language]["submissions"] += 1
#     command = input()
# print("Results:")
# for value in exam_results.values():
#     for person, points in value.items():
#         if person not in banned and person != "submissions":
#             print(f"{person} | {points}")
# print("Submissions:")
# for value, key in exam_results.items():
#     print(f"{value} - {exam_results[value]['submissions']}")
