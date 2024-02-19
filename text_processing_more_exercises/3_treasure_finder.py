import re


def find_message(decrypted_text_):
    matches = re.findall(r"[&](\w+)[&]", decrypted_text_)
    return matches[0] if matches else None


def find_coordinates(decrypted_text_):
    matches = re.findall(r"[<](\w+)[>]", decrypted_text_)
    return matches[0] if matches else None


def find_treasure(key_numbers_):
    result = []
    while True:
        decrypted_text = ''
        command = input()
        if command == "find":
            break

        text = command
        for i in range(len(text)):
            key = key_numbers_[i % len(key_numbers_)]
            char = text[i]
            ascii_number = ord(char)
            decrypted_char = chr(ascii_number - key)
            decrypted_text += decrypted_char

        current_type = find_message(decrypted_text)
        coordinates = find_coordinates(decrypted_text)

        result.append(f"Found {current_type} at {coordinates}\n")

    return ''.join(result)


key_numbers = [int(x) for x in input().split()]
treasure_found = find_treasure(key_numbers)
print(treasure_found)



# import re
# 
# 
# def find_message(decrypted_text_):
#     matches = re.findall(r"[&](\w+)[&]", decrypted_text_)
#     return matches[0] if matches else None
# 
# 
# def find_coordinates(decrypted_text_):
#     matches = re.findall(r"[<](\w+)[>]", decrypted_text_)
#     return matches[0] if matches else None
# 
# 
# key_numbers = [int(x) for x in input().split()]
# 
# 
# while True:
#     decrypted_text = ''
#     command = input()
#     if command == "find":
#         break
# 
#     text = command
#     for i in range(len(text)):
#         key = key_numbers[i % len(key_numbers)]
#         char = text[i]
#         ascii_number = ord(char)
#         decrypted_char = chr(ascii_number - key)
#         decrypted_text += decrypted_char
# 
#     current_type = find_message(decrypted_text)
#     coordinates = find_coordinates(decrypted_text)
# 
#     print(f"Found {current_type} at {coordinates}")





# keys_sequence = list(map(int, input().split()))
# string_sequence = input()
# result = []

# while string_sequence != 'find':
#     key_index = 0
#     for char in string_sequence:
#         key = keys_sequence[key_index]
#         result.append(chr(ord(char) - key))
#         key_index = (key_index + 1) % len(keys_sequence)
#     decoded_string = ''.join(result)

#     for i in range(1):
#         start_index_type = decoded_string.index('&') + 1
#         end_index_type = decoded_string.index('&', start_index_type)
#         type = decoded_string[start_index_type:end_index_type]
#         start_index_coordinates = decoded_string.index('<') + 1
#         end_index_coordinates = decoded_string.index('>')
#         coordinates = decoded_string[start_index_coordinates:end_index_coordinates]
#         print(f"Found {type} at {coordinates}")
#         result.clear()

#     string_sequence = input()
