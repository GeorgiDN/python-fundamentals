import re


def get_name(text):
    matches = re.findall(r"[@](\w+)[|]", text)
    return matches[0] if matches else None


def get_age(text):
    matches = re.findall(r"[#](\d+)[*]", text)
    return matches[0] if matches else None


def extract_person_information(rows_):
    persons_information_ = {}
    for _ in range(rows_):
        person_info = input()
        name = get_name(person_info)
        age = get_age(person_info)

        persons_information_[name] = age

    return persons_information_


def print_person_information(persons_information_):
    for curr_name, curr_age in persons_information_.items():
        print(f"{curr_name} is {curr_age} years old.")


rows = int(input())
persons_information = extract_person_information(rows)
print_person_information(persons_information)




#########################################################################################################
# import re
#
#
# def get_name(text):
#     pattern = "([@])([A-Za-z]+)([\|])"
#     matches = re.findall(pattern, text)
#     name_ = matches[0][1]
#     if matches:
#         return name_
#
#
# def get_age(text):
#     pattern = "([#])([\d]+)([\*])"
#     matches = re.findall(pattern, text)
#     age_ = matches[0][1]
#     if matches:
#         return age_
#
#
# def extract_person_information(persons_information_, rows_):
#     for _ in range(rows_):
#         person_info = input()
#         name = get_name(person_info)
#         age = get_age(person_info)
#         persons_information_[name] = age
#
#     return persons_information_
#
#
# def print_person_information(persons_information_):
#     for curr_name, curr_age in persons_information_.items():
#         print(f"{curr_name} is {curr_age} years old.")
#
#
# rows = int(input())
# persons_information = {}
# persons_information = extract_person_information(persons_information, rows)
# print_person_information(persons_information)



#################################################################################
# rows = int(input())
# for i in range(rows):
#     text = input()
#
#     start_index_name = text.index('@') + 1
#     end_index_name = text.index('|')
#     start_index_age = text.index('#') + 1
#     end_index_age = text.index('*')
#
#     name = text[start_index_name:end_index_name]
#     age = text[start_index_age:end_index_age]
#
#     print(f"{name} is {age} years old.")
