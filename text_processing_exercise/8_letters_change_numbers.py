text = input().split()
final_result = 0
for element in text:
    first_letter = element[0]
    last_letter = element[-1]
    number = int(element[1:-1])
    first_letter_position_in_alphabet = ord(first_letter.upper()) - 64
    last_letter_position_in_alphabet = ord(last_letter.upper()) - 64
    if first_letter.isupper():
        final_result += number / first_letter_position_in_alphabet
    else:
        final_result += number * first_letter_position_in_alphabet
    if last_letter.isupper():
        final_result -= last_letter_position_in_alphabet
    else:
        final_result += last_letter_position_in_alphabet
print(f"{final_result:.2f}")
