number = input()

digits = list(number)

digits.sort(reverse=True)

largest_number = int(''.join(digits))

print(largest_number)
