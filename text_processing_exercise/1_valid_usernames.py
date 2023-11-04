import re

usernames = input().split(', ')

pattern = r"^[a-zA-Z0-9_-]{3,16}$"

for username in usernames:
    if re.match(pattern, username):
        print(username)
