pokemons_list = [int(x) for x in input().split(" ")]
removed_elements = []

while pokemons_list:
    curr_index = int(input())

    removed_number = 0

    if curr_index < 0:
        curr_index = 0
        removed_number = pokemons_list.pop(0)
        last_element = pokemons_list[-1]
        pokemons_list.insert(0, last_element)
    elif curr_index >= len(pokemons_list):
        curr_index = len(pokemons_list) - 1
        removed_number = pokemons_list.pop(curr_index)
        first_element = pokemons_list[0]
        pokemons_list.insert(curr_index, first_element)
    else:
        removed_number = pokemons_list.pop(curr_index)

    removed_elements.append(removed_number)

    pokemons_list = [pokemon + removed_number if pokemon <= removed_number else pokemon - removed_number for pokemon in pokemons_list]

print(sum(removed_elements))



# numbers_sequence = list(map(int, input().split()))
# removed_pokemons = []
# while len(numbers_sequence) > 0:
#     current_index = int(input())
#     if current_index < 0:
#         removed = numbers_sequence[0]
#         numbers_sequence[0] = numbers_sequence[-1]
#     elif current_index >= len(numbers_sequence):
#         removed = numbers_sequence[-1]
#         numbers_sequence[-1] = numbers_sequence[0]
#     else:
#         removed = numbers_sequence.pop(current_index)
#     removed_pokemons.append(removed)
#     result_list = []
#     for number in numbers_sequence:
#         if number <= removed:
#             result_list.append(number + removed)
#         else:
#             result_list.append(number - removed)
#     numbers_sequence = result_list.copy()
# print(sum(removed_pokemons))
