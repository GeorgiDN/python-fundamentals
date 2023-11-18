import re

text = input()

#pattern = r"([=/])([A-Z][a-zA-Z]{2,})(?=\1)"
pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, text)

valid_destinations = [(match[1]) for match in matches]

destinations = ", ".join(valid_destinations)
travel_points = sum(len(match) for match in valid_destinations)

print(f"Destinations: {destinations}")
print(f"Travel Points: {travel_points}")
