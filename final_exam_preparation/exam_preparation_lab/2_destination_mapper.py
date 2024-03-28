import re

text = input()
pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, text)
destinations = [match[1] for match in matches]
travel_points = sum(len(match[1]) for match in matches)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")



# import re
# matches = re.findall(r"(=|\/)([A-Z][a-zA-Z]{2,})\1", input())
# print(f"Destinations: {', '.join([match[1] for match in matches])}\nTravel Points: {sum(len(match[1]) for match in matches)}")
