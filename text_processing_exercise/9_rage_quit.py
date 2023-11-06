unique_symbols = 0
gamer_input = input()
result_string = ''
current_string = ''
repetitions = 0

for idx, symbol in enumerate(gamer_input):
    if symbol.isdigit():
        if (idx + 1) < len(gamer_input):
            if gamer_input[idx + 1].isdigit():
                repetitions = int(symbol) * 10 + int(gamer_input[idx + 1])
                if current_string != '':
                    result_string += current_string * repetitions
                    current_string = ''
        if current_string != '':
            repetitions = int(symbol)
            result_string += current_string * repetitions
        current_string = ''
    else:
        if symbol.isalpha():
            current_string += symbol.upper()
        else:
            current_string += symbol

result_list = [el for el in result_string]
print(f"Unique symbols used: {len(set(result_list))}")
print(result_string)
