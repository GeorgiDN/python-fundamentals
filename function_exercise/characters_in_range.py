def characters_in_range(*args):
    return print(*[chr(i) for i in range(ord(args[0]) + 1, ord(args[1]))])


first = input()
second = input()

characters_in_range(first, second)


# def print_chars_between(start, end):
#     start_code = ord(start) + 1
#     end_code = ord(end)

#     for code in range(start_code, end_code):
#         char = chr(code)
#         print(char, end=" ")

# start_char = input()
# end_char = input()

# print_chars_between(start_char, end_char)
