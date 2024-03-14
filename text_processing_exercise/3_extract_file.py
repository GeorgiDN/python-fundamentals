import re

file_path = input()

pattern = r'\\([^\\]+)\.([^.]+)$'
matches = re.findall(pattern, file_path)

if matches:
    file_name, file_extension = matches[0]

    print(f"File name: {file_name}")
    print(f"File extension: {file_extension}")



# import re

# file_path = input()

# pattern = re.compile(r'\\([^\\]+)\.([^.]+)$')
# matches = pattern.findall(file_path)

# if matches:
#     file_name, file_extension = matches[0]

#     print(f"File name: {file_name}")
#     print(f"File extension: {file_extension}")




#######################################################

# file_path = input()
#
# last_backslash = file_path.rfind("\\")
# dot_position = file_path.rfind(".")
# file_name = file_path[last_backslash + 1:dot_position]
# file_extension = file_path[dot_position + 1:]
#
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")





################################
# import re
#
# file_path = input()
#
# pattern = re.compile(r'\\([^\\]+)\.([^.]+)$')
# match = pattern.search(file_path)
#
# if match:
#     file_name = match.group(1)
#     file_extension = match.group(2)
#
#     print(f"File name: {file_name}")
#     print(f"File extension: {file_extension}")



###########################
# file_path = input()
# last_index_backslash = 0
# last_index_point = 0
#
# for i, char in enumerate(file_path):
#     if char == "\\":
#         if i > last_index_backslash:
#             last_index_backslash = i
#     elif char == ".":
#         if i > last_index_point:
#             last_index_point = i
#
# file_name = file_path[last_index_backslash + 1:last_index_point]
# file_extension = file_path[last_index_point + 1:]
#
# print(f"File name: {file_name}\n"
#       f"File extension: {file_extension}")
