coffees_counter = 0

while True:
    event = input()
    if event == 'END':
        break
    if event == "coding" or event == 'dog' or event == 'cat' or event == 'movie':
        coffees_counter += 1
    elif event == "CODING" or event == 'DOG' or event == 'CAT' or event == 'MOVIE':
        coffees_counter += 2

if coffees_counter > 5:
    print('You need extra sleep')
else:
    print(coffees_counter)
