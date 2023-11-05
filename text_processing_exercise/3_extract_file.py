file_path = input()


last_backslash = file_path.rfind("\\")
# directory = file_path[:last_backslash]


dot_position = file_path.rfind(".")
file_name = file_path[last_backslash + 1:dot_position]
file_extension = file_path[dot_position + 1:]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
