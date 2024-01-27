substrings_input = [x for x in input().split(", ")]
words = [x for x in input().split(", ")]

substring_in_words = []
for substring in substrings_input:
    for word in words:
        if substring in word:
            substring_in_words.append(substring)
            break

print(substring_in_words)



# substrings_input = [x for x in input().split(", ")]
# words = [x for x in input().split(", ")]
# substring_in_words = [substring for substring in substrings_input for word in words if substring in word]
# checked_substrings = []
#
# for substring in substring_in_words:
#     if substring not in checked_substrings:
#         checked_substrings.append(substring)
#
# print(checked_substrings)


# first_line = input().split(', ')
# second_line = input().split(', ')

# check_list = []

# for substring in first_line:
#     for word in second_line:
#         if substring in word:
#             check_list.append(substring)
#             break

# print(check_list)
