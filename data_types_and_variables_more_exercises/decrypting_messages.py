def decrypt_message(key, lines):
    decrypted_message = ""
    for line in lines:
        for char in line:
            decrypted_char = chr(ord(char) + key)
            decrypted_message += decrypted_char
    return decrypted_message


key = int(input())
n = int(input())


lines = []
for _ in range(n):
    line = input()
    lines.append(line)


result = decrypt_message(key, lines)
print(result)







# key = int(input())
# n = int(input())
# lines = []

# for _ in range(n):
#     line = input()
#     lines.append(line)

# decrypted_message = ""
# for line in lines:
#     for char in line:
#         decrypted_char = chr(ord(char) + key)
#         decrypted_message += decrypted_char

# print(decrypted_message)
