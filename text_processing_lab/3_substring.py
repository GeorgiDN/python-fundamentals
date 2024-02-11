def substring_task():
    curr_substring = input()
    current_string = input()
    while curr_substring in current_string:
        current_string = current_string.replace(curr_substring, '')
    print(current_string)


substring_task()


# first_string = input()
# second_string = input()

# while first_string in second_string:
#     second_string = second_string.replace(first_string, '')

# print(second_string)
