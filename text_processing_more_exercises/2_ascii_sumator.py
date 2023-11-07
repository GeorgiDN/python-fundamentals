first_char = input()
sec_char = input()
string = input()

start_char = ord(first_char)
end_char = ord(sec_char)

total_sum = 0

for ch in string:
    if start_char < ord(ch) < end_char:
        total_sum += ord(ch)

print(total_sum)
