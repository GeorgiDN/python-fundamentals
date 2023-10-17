version = list(map(int, input().split('.')))
next_version = ""

if version[2] < 9:
    next_version = f'{version[0]}.{version[1]}.{version[2] + 1}'
elif version[1] < 9:
    next_version = f'{version[0]}.{version[1] + 1}.0'
else:
    next_version = f'{version[0] + 1}.0.0'

print(next_version)
