import re

info = input()
pattern = r"([#@])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
matches = re.finditer(pattern, info)
pairs_found = []
same_words_reversed = []

for match in matches:
    first_word = match.group(2)
    second_word = match.group(3)
    if first_word[::-1] == second_word:
        same_words_reversed.append(f"{first_word} <=> {second_word}")

    pairs_found.append(first_word)

if pairs_found:
    print(f"{len(pairs_found)} word pairs found!")
elif not pairs_found:
    print("No word pairs found!")


if same_words_reversed:
    print("The mirror words are:")
    print(", ".join(same_words_reversed))
elif not same_words_reversed:
    print("No mirror words!")
