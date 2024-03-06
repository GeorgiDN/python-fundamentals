import re

text = input()
pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, text)

destinations = [match[1] for match in matches]
print(f"Destinations: {', '.join(map(str, destinations))}")
travel_points = sum(len(word) for word in destinations)
print(f"Travel Points: {travel_points}")




# import re
#
#
# def find_valid_destinations(text):
#     pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
#     matches = re.findall(pattern, text)
#
#     valid_destinations = [(match[1]) for match in matches]
#
#     destinations = ", ".join(valid_destinations)
#     travel_points = sum(len(match) for match in valid_destinations)
#
#     print(f"Destinations: {destinations}")
#     print(f"Travel Points: {travel_points}")
#
#
# data = input()
# find_valid_destinations(data)




# import re
#
# text = input()
#
# #pattern = r"([=/])([A-Z][a-zA-Z]{2,})(?=\1)"
# pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
# matches = re.findall(pattern, text)
#
# valid_destinations = [(match[1]) for match in matches]
#
# destinations = ", ".join(valid_destinations)
# travel_points = sum(len(match) for match in valid_destinations)
#
# print(f"Destinations: {destinations}")
# print(f"Travel Points: {travel_points}")
