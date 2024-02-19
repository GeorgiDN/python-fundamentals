import re


class TreasureFinder:
    def __init__(self, key_numbers):
        self.key_numbers = key_numbers
        self.info_about_treasure = []

    def find_treasure(self):
        while True:
            decrypted_text = ''
            command = input()
            if command == "find":
                break

            text = command
            for i in range(len(text)):
                key = self.key_numbers[i % len(self.key_numbers)]
                char = text[i]
                ascii_number = ord(char)
                decrypted_char = chr(ascii_number - key)
                decrypted_text += decrypted_char

            current_type = self._find_message(decrypted_text)
            coordinates = self._find_coordinates(decrypted_text)

            self.info_about_treasure.append(f"Found {current_type} at {coordinates}\n")

        return ''.join(self.info_about_treasure)

    #### Helper methods
    def _find_message(self, decrypted_text_):
        matches = re.findall(r"[&](\w+)[&]", decrypted_text_)
        return matches[0] if matches else None

    def _find_coordinates(self, decrypted_text_):
        matches = re.findall(r"[<](\w+)[>]", decrypted_text_)
        return matches[0] if matches else None


numbers_with_key = [int(x) for x in input().split()]
treasure_finder = TreasureFinder(numbers_with_key)
print(treasure_finder.find_treasure())


#######################################################################################################################################
# import re
# 
# 
# def get_name(text):
#     matches = re.findall(r"[@](\w+)[|]", text)
#     return matches[0] if matches else None
# 
# 
# def get_age(text):
#     matches = re.findall(r"[#](\d+)[*]", text)
#     return matches[0] if matches else None
# 
# 
# def extract_person_information(rows_):
#     persons_information_ = {}
#     for _ in range(rows_):
#         person_info = input()
#         name = get_name(person_info)
#         age = get_age(person_info)
# 
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
# persons_information = extract_person_information(rows)
# print_person_information(persons_information)





#############################################################################################################################################
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



#######################################################################################################################################
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
