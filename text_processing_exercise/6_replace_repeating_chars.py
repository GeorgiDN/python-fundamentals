text = input()
final_string = text[0]

for i in range(1, len(text)):
    if text[i] != text[i - 1]:
        final_string += text[i]

print(final_string)



# string_input = input()
# final_string = ""
# 
# for i in range(len(string_input)):
#     char = string_input[i]
#     if not final_string:
#         final_string += char
#     elif final_string[-1] != char:
#         final_string += char
# 
# print(final_string)


# text = input()
# text_list = list(text)
# 
# check_symbols = []
# 
# for ch in text_list:
#     if ch not in check_symbols:
#         check_symbols.append(ch)
#     if check_symbols[-1] != ch:
#         check_symbols.append(ch)
# 
# print(''.join(check_symbols))
