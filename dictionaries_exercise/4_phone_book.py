phonebook = {}

while True:
    entry = input()
    if entry.isdigit():
        search_count = int(entry)
        break

    name, number = entry.split("-")
    phonebook[name] = number

searched_names = []
for _ in range(search_count):
    name_to_search = input()
    searched_names.append(name_to_search)

for name in searched_names:
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")

