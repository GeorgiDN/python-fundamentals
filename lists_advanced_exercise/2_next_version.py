version = input().split(".")
num1, num2, num3 = int(version[0]), int(version[1]), int(version[2])

num3 += 1
if num3 >= 9:
    num3 = 0
    num2 += 1
    if num2 == 10:
        num2 = 0
        num1 += 1

print(f"{num1}.{num2}.{num3}")



# version = list(map(int, input().split('.')))
# next_version = ""

# if version[2] < 9:
#     next_version = f'{version[0]}.{version[1]}.{version[2] + 1}'
# elif version[1] < 9:
#     next_version = f'{version[0]}.{version[1] + 1}.0'
# else:
#     next_version = f'{version[0] + 1}.0.0'

# print(next_version)



# version = list(map(int, input().split('.')))

# version[2] += 1

# if version[2] > 9:
#     version[2] = 0
#     version[1] += 1

# if version[1] > 9:
#     version[1] = 0
#     version[0] += 1

# next_version = '.'.join(map(str, version))
# print(next_version)
