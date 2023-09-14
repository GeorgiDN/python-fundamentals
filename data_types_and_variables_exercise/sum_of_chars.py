n = int(input())

sum_of_all_letters = 0

for _ in range(n):
    letter = input()
    number = ord(letter)
    sum_of_all_letters += int(number)

print(f'The sum equals: {sum_of_all_letters}')
