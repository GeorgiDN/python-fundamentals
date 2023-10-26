elements = input().split(" ")
keys = elements[::2]  
values = elements[1::2]  
bakery = dict(zip(keys, map(int, values)))

print(bakery)
