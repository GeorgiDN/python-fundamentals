first_line = input().split(', ')
second_line = input().split(', ')

check_list = []

for substring in first_line:
    for word in second_line:
        if substring in word:
            check_list.append(substring)
            break

print(check_list)
