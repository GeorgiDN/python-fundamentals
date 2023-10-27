elements = input().split(", ")
my_dict = {}

for i in range(0, len(elements)):
    key = elements[i]
    value = ord(key)
    my_dict[key] = int(value)

print(my_dict)
