import re


def extract_numbers(text_):
    matches = re.findall(r"\d+", text_)
    if matches:
        return matches


extracted_numbers = []
while True:
    text = input()
    if text == "":
        break

    found_number = extract_numbers(text)
    if found_number:
        extracted_numbers.extend(found_number)

print(*extracted_numbers)


# import re

# numbers = []

# while True:
#     txt = input()
#     if txt == "":
#         break

#     numbers.extend(re.findall(r'\d+', txt))

# print(' '.join(numbers))
