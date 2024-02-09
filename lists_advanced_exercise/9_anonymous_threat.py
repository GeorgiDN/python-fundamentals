def merge(list_name, start_index, end_index):
    if start_index < 0:
        start_index = 0
    list_with_result = list_name[:start_index]
    merged_element = ""
    index_in_range = True
    if end_index >= len(list_name):
        end_index = len(list_name) - 1
        index_in_range = False
    for index in range((end_index + 1) - start_index):
        current_index = index + start_index
        merged_element += list_name[current_index]
    list_with_result.append(merged_element)
    if index_in_range:
        list_with_result += list_name[(end_index + 1):]
    return list_with_result


def divide(list_name, index, partitions):
    result_list = list_name[:index]
    string_to_divide = list_name[index]
    current_substring = ""
    last_substring = ""
    letters_in_partition = len(string_to_divide) // partitions
    
    if len(string_to_divide) % partitions != 0:
        slice_index = (partitions - 1) * letters_in_partition
        last_substring = string_to_divide[slice_index:]
        string_to_divide = string_to_divide[:slice_index]
    for letter in string_to_divide:
        current_substring += letter
        if len(current_substring) == letters_in_partition:
            result_list.append(current_substring)
            current_substring = ""
    if last_substring != "":
        result_list.append(last_substring)
    if (index + 1) < len(list_name):
        result_list += list_name[index + 1:]
    return result_list


def anonymous_threat():
    data_array = input().split()
    while True:
        command = input()
        if command == "3:1":
            break
        info = command.split()
        
        current_command = info[0]
        first_value = int(info[1])
        second_value = int(info[2])
        if current_command == "merge":
            data_array = merge(data_array, first_value, second_value)
        elif current_command == "divide":
            data_array = divide(data_array, first_value, second_value)

    print(" ".join(data_array))


anonymous_threat()





# def merge_element(elements, start, end):
#     merge_result = ""
#     for i in range(start, end + 1):
#         merge_result += elements[i]

#     return merge_result


# words = input().split()

# while True:
#     line = input()
#     if line == "3:1":
#         break

#     command, first_arg, second_arg = line.split()
#     if command == "merge":
#         start_index, end_index = int(first_arg), int(second_arg)

#         start_index = max(0, start_index)
#         end_index = min(len(words) - 1, end_index)

#         if start_index >= end_index:
#             continue

#         merged_element = merge_element(words, start_index, end_index)
#         remove_count_ops = end_index - start_index + 1
#         for _ in range(remove_count_ops):
#             words.pop(start_index)
#         words.insert(start_index, merged_element)

#     elif command == "divide":
#         el_idx = int(first_arg)
#         partitions = int(second_arg)

#         element = words[el_idx]
#         elements_parts = []
#         partition_size = len(element) // partitions

#         current_partition = ''
#         for idx in range((partitions - 1) * partition_size):
#             current_partition += element[idx]
#             if len(current_partition) == partition_size:
#                 elements_parts.append(current_partition)
#                 current_partition = ''

#         current_partition = ''
#         for idx_ in range((partitions - 1) * partition_size, len(element)):
#             current_partition += element[idx_]

#         elements_parts.append(current_partition)

#         words.pop(el_idx)

#         for index_ in range(len(elements_parts)):
#             words.insert(el_idx + index_, elements_parts[index_])

# print(" ".join(words))












# 70/100
# data = input().split()
# commands = []
#
#
# while True:
#     command = input()
#     if command == "3:1":
#         break
#     commands.append(command)
#
#
# for command in commands:
#     tokens = command.split()
#     action = tokens[0]
#
#     if action == "merge":
#         start_index = int(tokens[1])
#         end_index = int(tokens[2])
#
#
#         start_index = max(0, start_index)
#         end_index = min(end_index, len(data) - 1)
#
#         merged = ''.join(data[start_index:end_index + 1])
#         data[start_index] = merged
#         del data[start_index + 1:end_index + 1]
#
#     elif action == "divide":
#         index = int(tokens[1])
#         partitions = int(tokens[2])
#         substring = data[index]
#
#         partition_size = len(substring) // partitions
#         divided = [substring[i:i + partition_size] for i in range(0, len(substring), partition_size)]
#
#
#         if len(divided) > partitions:
#             last_partition = divided[-1] + divided[-2]
#             divided.pop()
#             divided[-1] = last_partition
#
#         data.pop(index)
#         data[index:index] = divided
#
#
# print(' '.join(data))

