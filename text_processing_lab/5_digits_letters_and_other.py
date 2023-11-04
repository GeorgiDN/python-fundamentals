text = input()
text_list = list(text)

digits = ''
letters = ''
others = ''

for i in text_list:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        others += i

print(digits)
print(letters)
print(others)
