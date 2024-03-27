import re

text = input()
pattern = r'(^|\s)(-?\d+(\.\d+)?)(?=$|\s)'
matches = re.findall(pattern, text)

for match in matches:
    print(match[1], end=' ')



# import re

# # pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
# pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
# text = input()

# matches = re.finditer(pattern, text)

# for match in matches:
#     print(match.group(), end=' ')
