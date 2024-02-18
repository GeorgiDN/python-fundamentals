def add_char_to_substring(char_, substring_):
    if char_.isalpha():
        substring_ += char_.upper()
    else:
        substring_ += char_
    return substring_


def put_the_char_in_the_substring(char_, substring_):
    if char_.isalpha():
        substring_ = char_.upper()
    else:
        substring_ = char_

    return substring_


def fill_the_final_string(final_string_, characters_data_):
    final_string_ = ''
    for element in characters_data_:
        data = element.split()
        word, value = data[0], int(data[1])
        result = word * value
        final_string_ += result

    return final_string_


def main():
    text = input()
    substring = ""
    characters_data = []
    final_string = ""
    number = ''

    for char in text:
        if not char.isdigit():
            substring = add_char_to_substring(char, substring)
            if len(number) > 0:
                substring = substring[:-1]
                characters_data.append(f"{substring} {int(number)}")
                number = ''
                substring = put_the_char_in_the_substring(char, substring)
                continue
        elif char.isdigit():
            number += char

    if substring:
        characters_data.append(f"{substring} {int(number)}")

    final_string = fill_the_final_string(final_string, characters_data)
    unique_symbols_number = len(set(final_string))

    final_result = []
    final_result.append(f"Unique symbols used: {unique_symbols_number}")
    final_result.append("\n" + final_string)
    return print(''.join(final_result))


if __name__ == "__main__":
    main()




# unique_symbols = 0
# gamer_input = input()
# result_string = ''
# current_string = ''
# repetitions = 0

# for idx, symbol in enumerate(gamer_input):
#     if symbol.isdigit():
#         if (idx + 1) < len(gamer_input):
#             if gamer_input[idx + 1].isdigit():
#                 repetitions = int(symbol) * 10 + int(gamer_input[idx + 1])
#                 if current_string != '':
#                     result_string += current_string * repetitions
#                     current_string = ''
#         if current_string != '':
#             repetitions = int(symbol)
#             result_string += current_string * repetitions
#         current_string = ''
#     else:
#         if symbol.isalpha():
#             current_string += symbol.upper()
#         else:
#             current_string += symbol

# result_list = [el for el in result_string]
# print(f"Unique symbols used: {len(set(result_list))}")
# print(result_string)
