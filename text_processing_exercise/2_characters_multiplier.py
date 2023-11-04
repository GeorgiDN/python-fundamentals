str1, str2 = input().split()

total_sum = 0

min_length = min(len(str1), len(str2))

for i in range(min_length):
    total_sum += ord(str1[i]) * ord(str2[i])

if len(str1) > len(str2):
    for i in range(min_length, len(str1)):
        total_sum += ord(str1[i])
else:
    for i in range(min_length, len(str2)):
        total_sum += ord(str2[i])

print(total_sum)
