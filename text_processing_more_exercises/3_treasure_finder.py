keys_sequence = list(map(int, input().split()))
string_sequence = input()
result = []

while string_sequence != 'find':
    key_index = 0
    for char in string_sequence:
        key = keys_sequence[key_index]
        result.append(chr(ord(char) - key))
        key_index = (key_index + 1) % len(keys_sequence)
    decoded_string = ''.join(result)

    for i in range(1):
        start_index_type = decoded_string.index('&') + 1
        end_index_type = decoded_string.index('&', start_index_type)
        type = decoded_string[start_index_type:end_index_type]
        start_index_coordinates = decoded_string.index('<') + 1
        end_index_coordinates = decoded_string.index('>')
        coordinates = decoded_string[start_index_coordinates:end_index_coordinates]
        print(f"Found {type} at {coordinates}")
        result.clear()

    string_sequence = input()
