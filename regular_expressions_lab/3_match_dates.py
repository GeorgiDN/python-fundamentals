import re

dates = input()
pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'

matches = re.finditer(pattern, dates)

for match in matches:
    day = match.group(1)
    separator = match.group(2)
    month = match.group(3)
    year = match.group(4)
    print(f'Day: {day}, Month: {month}, Year: {year}')




# import re
# pattern = r"\b(?P<day>\d{2})([-./])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
# text = input()
# matches = re.finditer(pattern, text)
#
# for match in matches:
#     print(f'Day: {match["day"]}, Month: {match["month"]}, Year: {match["year"]}')
