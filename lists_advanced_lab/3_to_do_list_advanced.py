list_with_notes = {}
while True:
    command = input()
    if command == "End":
        break
    importance, note = command.split("-")
    importance = int(importance)
    if note not in list_with_notes:
        list_with_notes[importance] = note


sorted_priorities = dict(sorted(list_with_notes.items()))
to_do_list = [val for key, val in sorted_priorities.items()]
print(to_do_list)



# notes = [0] * 10
#
# while True:
#     command = input()
#     if command == 'End':
#         break
#
#     tokens = command.split('-')
#     priority = int(tokens[0]) - 1
#     note = tokens[1]
#     notes.pop(priority)
#     notes.insert(priority, note)
#
# result = [element for element in notes if element != 0]
# print(result)
#


