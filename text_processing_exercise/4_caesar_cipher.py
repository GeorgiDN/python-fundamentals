text = input()
decipher_text = ""
for char in text:
    letter = chr(ord(char) + 3)
    decipher_text += letter

print(decipher_text)


# def encrypt(message):
#     encrypted_message = ''
#     key = 3

#     for char in message:
#         encrypted_char = chr(ord(char) + key)
#         encrypted_message += encrypted_char

#     return encrypted_message

# line = input()

# print(encrypt(line))



# line = input()
# encrypted_message = ''
# key = 3
#
# for char in line:
#     encrypted_char = chr(ord(char) + key)
#     encrypted_message += encrypted_char
#
# print(encrypted_message)
