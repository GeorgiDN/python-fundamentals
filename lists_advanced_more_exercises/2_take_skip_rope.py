text = list(input())

number_list = [int(char) for char in text if char.isdigit()]
non_number_list = [char for char in text if not char.isdigit()]

take_list = [number for idx, number in enumerate(number_list) if idx % 2 == 0]
skip_list = [number for idx, number in enumerate(number_list) if idx % 2 != 0]
result = []

for i in range(len(take_list)):
    taken_characters = non_number_list[:take_list[i]]
    non_number_list = non_number_list[take_list[i] + skip_list[i]:]
    result.extend(taken_characters)

final_result = ''.join(result)
print(final_result)


# input_string = input()
# input_list = list(input_string)

# number_list = []
# non_number_list = []

# for char in input_list:
#     if char.isdigit():
#         number_list.append(char)
#     else:
#         non_number_list.append(char)

# number_list = list(map(int, number_list))  # all numbers
# take_list = []  
# skip_list = []  

# for index, num in enumerate(number_list):
#     if index % 2 == 0:
#         take_list.append(num)
#     else:
#         skip_list.append(num)

# taken_string = []

# for i in range(len(take_list)):
#     taken_characters = non_number_list[:take_list[i]]
#     non_number_list = non_number_list[take_list[i] + skip_list[i]:]
#     taken_string.extend(taken_characters)

# final_result = ''.join(taken_string)
# print(final_result)
