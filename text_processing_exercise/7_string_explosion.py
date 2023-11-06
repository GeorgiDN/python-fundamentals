text = input()
compressed_text = []
strength = 0
i = 0

while i < len(text):
    compressed_text.append(text[i])
    if text[i].isdigit():
        strength += int(text[i])

    if strength > 0 and text[i] != '>':
        compressed_text.pop()
        strength -= 1

    i += 1

print(''.join(compressed_text))
