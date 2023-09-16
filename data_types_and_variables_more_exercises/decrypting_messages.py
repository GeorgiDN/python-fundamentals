def decrypt_message(key, lines):
    decrypted_message = ""
    for line in lines:
        for char in line:
            decrypted_char = chr(ord(char) + key)
            decrypted_message += decrypted_char
    return decrypted_message

# Въвеждане на ключа и броя на редовете
key = int(input())
n = int(input())

# Въвеждане на редовете
lines = []
for _ in range(n):
    line = input()
    lines.append(line)

# Извикване на функцията и отпечатване на резултата
result = decrypt_message(key, lines)
print(result)
