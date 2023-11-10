import re

text = input()
final_lst = []
regex = r'\b_[A-Za-z0-9]+\b'
matches = re.findall(regex, text)

for word in matches:
    new_word = word.replace('_', '')
    final_lst.append(new_word)

print(','.join(final_lst))
