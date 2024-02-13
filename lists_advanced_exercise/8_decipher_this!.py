string_input = input().split(" ")

decipher_string_1 = []
final_decipher_string = []

number = ''
for word in string_input:
    for char in word:
        if char.isdigit():
            number += char
        else:
            decipher_string_1.append(char)

    # find letter on the current number
    letter = chr(int(number))
    # insert letter in the beginning of string
    decipher_string_1.insert(0, letter)
    number = ''
    # swap second and last letter
    sec_letter = decipher_string_1[1]
    last_letter = decipher_string_1[-1]
    decipher_string_1[1] = last_letter
    decipher_string_1[-1] = sec_letter
    final_decipher_string.extend(decipher_string_1)
    final_decipher_string.extend(' ')
    decipher_string_1 = []

print(''.join(final_decipher_string))




# import re


# string_input = input().split(" ")

# decipher_string_1 = []
# final_decipher_string = []

# pattern = r"\d+"

# number = ''
# for word in string_input:
#     for char in word:
#         if re.match(pattern, char):
#             number += char
#         else:
#             decipher_string_1.append(char)

#     # find letter on the current number
#     letter = chr(int(number))
#     # insert letter in the beginning of string
#     decipher_string_1.insert(0, letter)
#     number = ''
#     # swap second and last letter
#     sec_letter = decipher_string_1[1]
#     last_letter = decipher_string_1[-1]
#     decipher_string_1[1] = last_letter
#     decipher_string_1[-1] = sec_letter
#     final_decipher_string.extend(decipher_string_1)
#     final_decipher_string.extend(' ')
#     decipher_string_1 = []

# print(''.join(final_decipher_string))





# my_list = input().split()
# my_number_list = []
# number_part = ''
# index = 0
#
# for item in my_list:
#     number_part = ''.join(filter(str.isdigit, item))
#     if number_part:
#         my_number_list.append(int(number_part))
#
#     numbers_str = ''.join(map(str, my_number_list))
#     result_number = int(numbers_str)
#     first_char = chr(result_number)  # H
#     remaining_text = my_list[0 + index].replace(number_part, '')  # Вземаме текста след числото
#
#     if len(remaining_text) >= 2:
#         # Размяна на първата и последната буква
#         swapped_text = remaining_text[-1] + remaining_text[1:-1] + remaining_text[0]
#     else:
#         swapped_text = remaining_text
#
#     result_text = first_char + swapped_text
#     my_number_list.pop()
#     number_part = ''
#     index += 1
#     print(result_text, end=' ')

