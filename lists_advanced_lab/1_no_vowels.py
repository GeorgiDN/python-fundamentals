text = input()
print(''.join([letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', "i"]]))


# text = input()
# sorted_text = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', "i"]]
# print(''.join(sorted_text))



# text = input()
# sorted_text = [letter for letter in text if letter not in ['a', 'o', 'u', 'e', 'i', 'A', 'E', 'I', 'O', 'U']]
# print(''.join(sorted_text))



# text = input()
# vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'E', 'I', 'O', 'U']
#
# letters_list = []
#
# for letter in text:
#     if letter not in vowels:
#           letters_list.append(letter)
#
# print(''.join(letters_list))
