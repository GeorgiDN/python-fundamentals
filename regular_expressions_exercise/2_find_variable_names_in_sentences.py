import re

text = input()
final_lst = []
regex = r'\b_[A-Za-z0-9]+\b'
matches = re.findall(regex, text)

for word in matches:
    new_word = word.replace('_', '')
    final_lst.append(new_word)

print(','.join(final_lst))




# import re

# txt = input()
# regex = r'\b_[A-Za-z\d]*\b'
# matches = re.findall(regex, txt)

# result = ",".join(matches)
# final_result = []
# for i in result:
#     if i != '_':
#         final_result.append(i)

# print(''.join(final_result))
