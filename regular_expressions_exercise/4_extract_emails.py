import re

text = input()
pattern = r"(^|(?<=\s))([a-z0-9]+[\.\-\_a-z]*)@([a-z\-]+)(\.[a-z]+)+\b"
emails = re.finditer(pattern, text)
print_emails = [email.group() for email in emails]
print(*print_emails, sep="\n")
