import re

text = input()
pattern = r"([@|#]+)([a-z]{3,})(@|#)([^A-Za-z\d]*)([\/]+)(\d+)([\/]+)"
matches = re.finditer(pattern, text)

for match in matches:
    color = match.group(2)
    amount = match.group(6)
    print(f"You found {amount} {color} eggs!")




#  Do not do this!
# import re
# for match in re.finditer(r"([@|#]+)([a-z]{3,})(@|#)([^A-Za-z\d]*)([\/]+)(\d+)([\/]+)", input()):print(f"You found {match.group(2)} {match.group(6)} eggs!")
