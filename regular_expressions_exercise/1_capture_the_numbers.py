import re

numbers = []

while True:
    txt = input()
    if txt == "":
        break

    numbers.extend(re.findall(r'\d+', txt))

print(' '.join(numbers))
