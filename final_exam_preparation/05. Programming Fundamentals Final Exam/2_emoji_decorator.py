import re
from functools import reduce


def find_cool_threshold(text_):
    found_digits = re.findall(r"\d", text_)
    found_digits = list((map(int, found_digits)))
    cool_threshold_ = reduce(lambda x, y: x * y, found_digits)
    return cool_threshold_


def take_all_emogies(found_emojies_, emojies_dict_):
    for emoji in found_emojies_:
        current_emoji = (emoji.group())
        sum_ascii_values = 0
        for char in current_emoji:
            if not char == ":" and not char == "*":
                sum_ascii_values += ord(char)

        if current_emoji not in emojies_dict:
            emojies_dict[current_emoji] = sum_ascii_values

    return emojies_dict_


def print_result(cool_threshold_, emojies_dict_):
    result = []
    result.append(f"Cool threshold: {cool_threshold_}\n")
    result.append(f"{len(emojies_dict_)} emojis found in the text. The cool ones are:\n")

    for name, points in emojies_dict_.items():
        if points > cool_threshold_:
            result.append(f"{name}\n")

    return print(''.join(result))


text = input()
emojies_dict = {}
cool_threshold = find_cool_threshold(text)
pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
found_emojies = re.finditer(pattern, text)

emojies_dict = take_all_emogies(found_emojies, emojies_dict)
print_result(cool_threshold, emojies_dict)
