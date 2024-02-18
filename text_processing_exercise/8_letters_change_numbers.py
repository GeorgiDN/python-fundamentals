def find_letter_position_in_alphabet_starting_from_one(letter):
    letter = ord(letter.lower()) - 96
    return letter


def main():
    text = input().split()
    result = 0
    
    for element in text:
        first_letter = element[0]
        last_letter = element[-1]
        number = int(element[1:-1])
        first_letter_position = find_letter_position_in_alphabet_starting_from_one(first_letter)
        last_letter_position = find_letter_position_in_alphabet_starting_from_one(last_letter)
        if first_letter.isupper():
            result += number / first_letter_position
        else:
            result += number * first_letter_position
        if last_letter.isupper():
            result -= last_letter_position
        else:
            result += last_letter_position
    
    print(f"{result:.2f}")


if __name__ == "__main__":
    main()


#
# text = input().split()
# result = 0

# for element in text:
#     first_letter = element[0]
#     last_letter = element[-1]
#     number = int(element[1:-1])
#     first_letter_position = ord(first_letter.lower()) - 96
#     last_letter_position = ord(last_letter.lower()) - 96
#     if first_letter.isupper():
#         result += number / first_letter_position
#     else:
#         result += number * first_letter_position
#     if last_letter.isupper():
#         result -= last_letter_position
#     else:
#         result += last_letter_position

# print(f"{result:.2f}")
