import re

pattern = r"(w{3}.([a-zA-Z0-9-]+)((\.[a-z]+)+))"

while True:
    line = input()
    if line == "":
        break

    link = re.findall(pattern, line)
    if link:
        print(link[0][0])


        
# import re
# 
# text = input()
# while text:
#     pattern = r"((w{3})\.([A-Za-z0-9]+)([A-Za-z0-9\-]+)*(\.[a-z]+)+)"
#     matched_links = re.search(pattern, text)
#     if matched_links:
#         print(matched_links.group())
#     text = input()
