string_1, string_2 = input().split()
total_sum = 0
min_length = min(len(string_1), len(string_2))

total_sum += sum([ord(string_1[i]) * ord(string_2[i]) for i in range(min_length)])

if len(string_1) > len(string_2):
    total_sum += sum([ord(string_1[i]) for i in range(min_length, len(string_1))])
else:
    total_sum += sum([ord(string_2[i]) for i in range(min_length, len(string_2))])

print(total_sum)




# string_1, string_2 = input().split()
# total_sum = 0
# min_length = min(len(string_1), len(string_2))
#
# for i in range(min_length):
#     total_sum += ord(string_1[i]) * ord(string_2[i])
#
# if len(string_1) > len(string_2):
#     for i in range(min_length, len(string_1)):
#         total_sum += ord(string_1[i])
# else:
#     for i in range(min_length, len(string_2)):
#         total_sum += ord(string_2[i])
#
# print(total_sum)
