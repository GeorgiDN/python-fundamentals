my_list = []

for _ in range(3):
    data = input()
    my_list.append(data)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)


# tail = input()
# body = input()
# head = input()

# meerkat = [tail, body, head]

# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

# print(meerkat)
