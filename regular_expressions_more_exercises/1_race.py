import re

participants = input().split(", ")
race_results = {}
info = input()
while info != "end of race":
    name_pattern = r"[A-Za-z]"
    distance_pattern = r"[0-9]"
    name_match = re.findall(name_pattern, info)
    distance_match = re.findall(distance_pattern, info)
    name = "".join(name_match)
    distance = sum([int(x) for x in distance_match])
    if name in participants:
        if name not in race_results:
            race_results[name] = distance
        else:
            race_results[name] += distance
    info = input()
    
sorted_results = dict(sorted(race_results.items(), key=lambda x: -x[1]))
rank = 0
for name in sorted_results:
    rank += 1
    if rank > 3:
        break
    if rank == 1:
        current_rank = "1st"
    elif rank == 2:
        current_rank = "2nd"
    elif rank == 3:
        current_rank = "3rd"
    print(f"{current_rank} place: {name}")











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
