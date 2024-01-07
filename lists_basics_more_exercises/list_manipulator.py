import sys


def is_valid_index(lst, indx):
    return 0 <= indx < len(lst)


def exchange_list(lst, index):
    if is_valid_index(lst, index):
        first_sub_list = lst[:index + 1]
        second_sub_list = lst[index + 1:]
        return second_sub_list + first_sub_list
    else:
        print("Invalid index")
        return lst


def index_max_odd_element(lst):
    max_number = -sys.maxsize
    max_odd_index_ = 0
    matches_ = []
    for i, num in enumerate(lst):
        if num % 2 != 0:
            if num >= max_number:
                max_number = num
                max_odd_index_ = i
                matches_.append(max_odd_index_)
    if matches_:
        return max_odd_index_
    return "No matches"


def index_max_even_element(lst):
    max_number = -sys.maxsize
    max_even_index_ = 0
    matches_ = []
    for i, num in enumerate(lst):
        if num % 2 == 0:
            if num >= max_number:
                max_number = num
                max_even_index_ = i
                matches_.append(max_even_index_)
    if matches_:
        return max_even_index_
    return "No matches"


def index_min_odd_element(lst):
    min_number = sys.maxsize
    min_odd_index_ = 0
    matches = []
    for i, num in enumerate(lst):
        if num % 2 != 0:
            if num <= min_number:
                min_number = num
                min_odd_index_ = i
                matches.append(min_odd_index_)
    if matches:
        return min_odd_index_
    return "No matches"


def index_min_even_element(lst):
    min_number = sys.maxsize
    min_even_index_ = 0
    matches = []
    for i, num in enumerate(lst):
        if num % 2 == 0:
            if num <= min_number:
                min_number = num
                min_even_index_ = i
                matches.append(min_even_index_)
    if matches:
        return min_even_index_
    return "No matches"


def first_count_even(lst, countt):
    if countt > len(lst):
        return "Invalid count"
    matches = []
    for j, num in enumerate(lst):
        if num % 2 == 0:
            matches.append(num)
            if len(matches) == countt:
                return matches
    return matches


def first_count_odd(lst, countt):
    if countt > len(lst):
        return "Invalid count"
    matches = []
    for j, num in enumerate(lst):
        if num % 2 != 0:
            matches.append(num)
            if len(matches) == countt:
                return matches
    return matches


def last_count_even(lst, countt):
    if countt > len(lst):
        return "Invalid count"
    matches = []
    for j, num in enumerate(reversed(lst)):
        if num % 2 == 0:
            matches.append(num)
            if len(matches) == countt:
                return matches[::-1]
    return matches


def last_count_odd(lst, countt):
    if countt > len(lst):
        return "Invalid count"
    matches = []
    for j, num in enumerate(reversed(lst)):
        if num % 2 != 0:
            matches.append(num)
            if len(matches) == countt:
                return matches[::-1]
    return matches


manipulated_list = [int(x) for x in input().split(' ')]

while True:
    command = input()
    if command == 'end':
        break

    info = command.split(" ")
    action = info[0]

    if action == "exchange":
        index_ = int(info[1])
        manipulated_list = exchange_list(manipulated_list, index_)

    # Check max
    elif action == "max":
        kind = info[1]
        if kind == "odd":
            print(index_max_odd_element(manipulated_list))

        elif kind == "even":
            print(index_max_even_element(manipulated_list))

    # Check min
    elif action == "min":
        kind = info[1]
        if kind == "odd":
            print(index_min_odd_element(manipulated_list))

        elif kind == "even":
            print(index_min_even_element(manipulated_list))

    # First count
    elif action == "first":
        count_, kind_ = int(info[1]), info[2]
        if kind_ == "even":
            print(first_count_even(manipulated_list, count_))
        elif kind_ == "odd":
            print(first_count_odd(manipulated_list, count_))

    # Last count
    elif action == "last":
        count_, kind_ = int(info[1]), info[2]
        if kind_ == "even":
            print(last_count_even(manipulated_list, count_))
        elif kind_ == "odd":
            print(last_count_odd(manipulated_list, count_))


print(manipulated_list)
