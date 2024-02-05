def count_chars_in_string(chars_in_string):
    text = input()

    for char in text:
        if char.strip():
            if char not in chars_in_string:
                chars_in_string[char] = 0
            chars_in_string[char] += 1

    return chars_in_string


chars_in_text = {}
count_chars_in_string(chars_in_text)

print('\n'.join([f"{ch} -> {num}" for ch, num in chars_in_text.items()]))




# chars_in_string = {}
# text = input()
#
# for char in text:
#     if char.strip():
#         if char not in chars_in_string:
#             chars_in_string[char] = 0
#         chars_in_string[char] += 1
#
# print('\n'.join([f"{ch} -> {num}" for ch, num in chars_in_string.items()]))





# text = input()
# character_count = {}

# for char in text:
#     if char != " ":
#         if char in character_count:
#             character_count[char] += 1
#         else:
#             character_count[char] = 1

# for char, count in character_count.items():
#     print(f"{char} -> {count}")
  
