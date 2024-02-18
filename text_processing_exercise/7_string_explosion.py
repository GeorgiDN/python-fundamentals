text = list(input())
final_text = text[:2]

strength = 0

for idx in range(2, len(text)):
    char = text[idx]
    final_text.append(char)
    if final_text[-2] == ">" and final_text[-1] != ">":
        if char.isdigit():
            strength += int(char)
        if strength > 0:
            final_text.pop()
            strength -= 1

print(''.join(final_text))


# text = input()
# compressed_text = []
# strength = 0
# i = 0

# while i < len(text):
#     compressed_text.append(text[i])
#     if text[i].isdigit():
#         strength += int(text[i])

#     if strength > 0 and text[i] != '>':
#         compressed_text.pop()
#         strength -= 1

#     i += 1

# print(''.join(compressed_text))
