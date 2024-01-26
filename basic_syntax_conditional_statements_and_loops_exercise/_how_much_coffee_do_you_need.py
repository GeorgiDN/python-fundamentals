def take_input():
    return input()


def calculate_needed_coffee(lst_events):
    number_of_coffees = 0
    while True:
        event = take_input()
        if event == "END":
            break

        if event.lower() in lst_events:
            if event.isupper():
                number_of_coffees += 1
            number_of_coffees += 1

        if number_of_coffees > 5:
            return print("You need extra sleep")

    return print(number_of_coffees)


list_events = ["coding", "dog", "cat", "movie"]
calculate_needed_coffee(list_events)







# coffees_counter = 0

# while True:
#     event = input()
#     if event == 'END':
#         break
#     if event == "coding" or event == 'dog' or event == 'cat' or event == 'movie':
#         coffees_counter += 1
#     elif event == "CODING" or event == 'DOG' or event == 'CAT' or event == 'MOVIE':
#         coffees_counter += 2

# if coffees_counter > 5:
#     print('You need extra sleep')
# else:
#     print(coffees_counter)
