start_character = input()
end_character = input()
text = input()
total_sum = 0

range_start = ord(start_character)
range_end = ord(end_character)

for char in text:
    if ord(char) in range(range_start + 1, range_end):
        total_sum += ord(char)

print(total_sum)



# first_char = input()
# sec_char = input()
# string = input()

# start_char = ord(first_char)
# end_char = ord(sec_char)

# total_sum = 0

# for ch in string:
#     if start_char < ord(ch) < end_char:
#         total_sum += ord(ch)

# print(total_sum)
