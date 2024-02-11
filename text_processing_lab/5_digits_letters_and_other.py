def digits_letters_and_other():
    text = input()

    digits = [char for char in text if char.isdigit()]
    letters = [char for char in text if char.isalpha()]
    other = [char for char in text if not char.isalpha() and not char.isdigit()]

    print(''.join(digits))
    print(''.join(letters))
    print(''.join(other))


digits_letters_and_other()



# def digits_letters_and_other():
#     text = input()
#     digits = ""
#     letters = ""
#     other = ""
# 
#     for char in text:
#         if char.isdigit():
#             digits += char
#         elif char.isalpha():
#             letters += char
#         else:
#             other += char
# 
#     print(digits)
#     print(letters)
#     print(other)
# 
# 
# digits_letters_and_other()





# text = input()
# text_list = list(text)

# digits = ''
# letters = ''
# others = ''

# for i in text_list:
#     if i.isdigit():
#         digits += i
#     elif i.isalpha():
#         letters += i
#     else:
#         others += i

# print(digits)
# print(letters)
# print(others)
