import re

text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.finditer(pattern, text)
matches_2 = re.findall(pattern, text)
valid_matches = [match[1] for match in matches_2]
mirror_words = [f"{match.group(2)} <=> {match.group(3)}" for match in matches if match.group(2) == match.group(3)[::-1]]

print("No word pairs found!") if not valid_matches else print(f"{len(valid_matches)} word pairs found!")
print("No mirror words!") if not mirror_words else print(f"The mirror words are:\n{', '.join(mirror_words)}")





############################################################################################################################################
# import re


# def extract_matches(matches, mirror_words, word_pairs_found):
#     for match in matches:
#         word_pairs_found.append(match)
#         first_word = match.group(2)
#         second_word = match.group(3)
#         if first_word == second_word[::-1]:
#             mirror_words.append(f"{first_word} <=> {first_word[::-1]}")
#     return mirror_words, word_pairs_found


# def print_result(mirror_words, word_pairs_found):
#     result = ''
#     if not word_pairs_found:
#         result += "No word pairs found!\n"
#     else:
#         result += f"{len(word_pairs_found)} word pairs found!\n"

#     if not mirror_words:
#         result += "No mirror words!"
#     else:
#         result += f"The mirror words are:\n"
#         result += f"{', '.join(mirror_words)}"

#     return print(''.join(result))


# text = input()
# pattern = r"([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
# matches = re.finditer(pattern, text)
# mirror_words = []
# word_pairs_found = []
# mirror_words, word_pairs_found = extract_matches(matches, mirror_words, word_pairs_found)
# print_result(mirror_words, word_pairs_found)




###########################################################################################################################################
# import re
# 
# text = input()
# pattern = r"([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
# matches = re.finditer(pattern, text)
# mirror_words = []
# word_pairs_found = []
# 
# for match in matches:
#     word_pairs_found.append(match)
#     first_word = match.group(2)
#     second_word = match.group(3)
#     if first_word == second_word[::-1]:
#         mirror_words.append(f"{first_word} <=> {first_word[::-1]}")
# 
# if not word_pairs_found:
#     print("No word pairs found!")
# else:
#     print(f"{len(word_pairs_found)} word pairs found!")
# 
# if not mirror_words:
#     print("No mirror words!")
# else:
#     print(f"The mirror words are:\n"
#           f"{', '.join(mirror_words)}")

