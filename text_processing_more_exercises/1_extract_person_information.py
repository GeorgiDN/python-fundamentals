lines = int(input())
for i in range(lines):
    text = input()

    start_index_name = text.index('@') + 1
    end_index_name = text.index('|')
    start_index_age = text.index('#') + 1
    end_index_age = text.index('*')

    name = text[start_index_name:end_index_name]
    age = text[start_index_age:end_index_age]

    print(f"{name} is {age} years old.")
