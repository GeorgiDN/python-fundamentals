elements = input().split(" ")
keys = elements[::2]  
values = elements[1::2]  
bakery = dict(zip(keys, map(int, values)))

print(bakery)




# elements = input().split(" ")
# bakery = {}
#
# for i in range(0, len(elements), 2):
#     key = elements[i]
#     value = elements[i + 1]
#     bakery[key] = int(value)
#
# print(bakery)
