def phone_book_task():
    phone_book = {}
    while True:
        data = input()
        if data.isdigit():
            break
        info = data.split("-")
        name, number_ = info[0], info[1]
        phone_book[name] = number_

    searched_numbers = int(data)
    for _ in range(searched_numbers):
        searched_name = input()
        if searched_name in phone_book:
            print(''.join([f"{name_} -> {num}" for name_, num in phone_book.items() if searched_name == name_]))
        else:
            print(f"Contact {searched_name} does not exist.")


phone_book_task()


# phonebook = {}

# while True:
#     entry = input()
#     if entry.isdigit():
#         search_count = int(entry)
#         break

#     name, number = entry.split("-")
#     phonebook[name] = number

# searched_names = []
# for _ in range(search_count):
#     name_to_search = input()
#     searched_names.append(name_to_search)

# for name in searched_names:
#     if name in phonebook:
#         print(f"{name} -> {phonebook[name]}")
#     else:
#         print(f"Contact {name} does not exist.")

