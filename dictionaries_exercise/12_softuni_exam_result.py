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



