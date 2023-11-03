strings = input().split(' ')
result = ''
for word in strings:
    result += word * len(word)
print(result)


# data = input().split()
# new_text = [word * len(word) for word in data]
#
# print(''.join(new_text))
