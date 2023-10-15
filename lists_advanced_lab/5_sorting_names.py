string = input().split(', ')
sorted_list = sorted(string, key=lambda x: (-len(x), x))
print(sorted_list)
