import re

text = input()
pattern = r'\b_[A-Za-z0-9]+\b'
matches = re.findall(pattern, text)

found_variable = [re.sub("_", "", match) for match in matches]
print(','.join(found_variable))



########################################################################################
# import re
# print(','.join([re.sub("_", "", match) for match in re.findall(r'\b_[A-Za-z0-9]+\b', input())]))



#####################################################################################
# import re
#
# text = input()
# matches = re.findall(r'\b_[A-Za-z0-9]+\b', text)
# print(','.join([re.sub("_", "", match) for match in matches]))



#####################################################################################
# import re
#
# found_variable = []
# text = input()
# pattern = r'\b_[A-Za-z0-9]+\b'
# matches = re.findall(pattern, text)
#
# for match in matches:
#     variable_name = re.sub("_", "", match)
#     found_variable.append(variable_name)
#
# print(','.join(found_variable))



#####################################################################################
# import re
#
# text = input()
# final_lst = []
# regex = r'\b_[A-Za-z0-9]+\b'
# matches = re.findall(regex, text)
#
# for word in matches:
#     new_word = word.replace('_', '')
#     final_lst.append(new_word)
#
# print(','.join(final_lst))
