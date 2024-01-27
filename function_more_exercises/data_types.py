def data_types_implementation(kind, char):
    if kind == "int":
        return int(char) * 2
    if kind == "real":
        return f"{(float(char) * 1.5):.02f}"
    if kind == "string":
        return f"${char}$"


current_kind = input()
current_string = input()
print(data_types_implementation(current_kind, current_string))



# def current_input(command, num):
#     result = None
#     if command == 'int':
#         num = int(num)
#         result = num * 2
#     elif command == 'real':
#         num = float(num)
#         result = num * 1.5
#         result = f'{result:.2f}'
#     elif command == 'string':
#         num = str(num)
#         result = f"${num}$"

#     return result

# determiners = input()
# user_input = input()

# print(current_input(determiners, user_input))
