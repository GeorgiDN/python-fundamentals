import re

text = input()
searched_word = input()

pattern = r'\b' + searched_word + r'\b'
x = re.findall(pattern, text, re.IGNORECASE)
print(len(x))
