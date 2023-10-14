text = input()
sorted_text = [letter for letter in text if letter not in ['a', 'o', 'u', 'e', 'i', 'A', 'E', 'I', 'O', 'U']]

print(''.join(sorted_text))
