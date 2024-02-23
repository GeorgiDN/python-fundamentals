import re


def extract_name_from_string(data_):
    pattern = r"[A-Za-z]+"
    matches = re.findall(pattern, data_)
    return ''.join(matches) if matches else None


def extract_numbers_from_string(data_):
    pattern = r"\d"
    matches = re.findall(pattern, data_)
    return sum(map(int, matches)) if matches else 0


def show_ranks(sorted_result_):
    final_results = []
    ranks = {1: "1st", 2: "2nd", 3: "3rd"}
    rank = 1
    for participant in sorted_result_:
        if rank > 3:
            break
        final_results.append(f"{ranks[rank]} place: {participant}\n")
        rank += 1

    return print(''.join(final_results))


def race():
    participants = input().split(", ")
    results = {}
    while True:
        data = input()
        if data == "end of race":
            break

        name = extract_name_from_string(data)
        distance = extract_numbers_from_string(data)
        if name in participants:
            if name not in results:
                results[name] = 0
            results[name] += distance

    sorted_result = dict(sorted(results.items(), key=lambda x: -x[1]))
    show_ranks(sorted_result)


race()









# name = ""
# sum_of_digits = 0
# ranking = {}
#
# participants = input().split(', ')
#
# while True:
#
#     text = input()
#     if text == 'end of race':
#         break
#
#     for char in text:
#         if char.isalpha():
#             name += char
#         elif char.isdigit():
#             sum_of_digits += int(char)
#
#     if name in participants:
#         if name not in ranking:
#             ranking[name] = sum_of_digits
#         else:
#             ranking[name] += sum_of_digits
#
#     name = ''
#     sum_of_digits = 0
#
# sorted_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
# rank = 1
# for name1, score in sorted_ranking[:3]:
#     if rank == 1:
#         print(f"{rank}st place: {name1}")
#     elif rank == 2:
#         print(f"{rank}nd place: {name1}")
#     elif rank == 3:
#         print(f"{rank}rd place: {name1}")
#     rank += 1
