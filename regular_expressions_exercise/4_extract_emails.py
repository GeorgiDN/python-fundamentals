import re

text = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
emails = re.findall(pattern, text)
for email in emails:
    print(email[0])




# import re
#
# text = input()
# pattern = r"(^|(?<=\s))([a-z0-9]+[\.\-\_a-z]*)@([a-z\-]+)(\.[a-z]+)+\b"
# emails = re.finditer(pattern, text)
# for email in emails:
#     current_email = email.group()
#     print(current_email)





# import re
#
# text = input()
# pattern = r"(^|(?<=\s))([a-z0-9]+[\.\-\_a-z]*)@([a-z\-]+)(\.[a-z]+)+\b"
# emails = re.finditer(pattern, text)
# print_emails = [email.group() for email in emails]
# print(*print_emails, sep="\n")



# import re
#
# txt = input()
# pattern = r"(^|(?<=\s))(?P<user>[a-zA-Z0-9]+[._-]?[a-zA-Z0-9]+)@" \
#           r"(?P<host>[a-zA-Z0-9]+[-]?[a-zA-Z0-9]+\.[a-zA-Z\.]{2,}\b)"
#
# mails = re.finditer(pattern, txt)
# for mail in mails:
#     print(f"{mail['user']}@{mail['host']}")
