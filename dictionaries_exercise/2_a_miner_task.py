command = input()
my_dictionary = {}

while command != 'stop':
    quantity = int(input())
    key = command
    value = quantity

    if key not in my_dictionary:
        my_dictionary[key] = int(value)
    else:
        my_dictionary[key] += int(value)

    command = input()

for key, value in my_dictionary.items():
    print(f"{key} -> {value}")
  
