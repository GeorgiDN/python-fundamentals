sequence = list(map(int, input().split()))
text = input()

message = ""
print(len(text))
for num in sequence:
    index = sum(map(int, str(num)))
    while index >= len(text):
        index -= len(text)
    message += text[index]
    text = text[:index] + text[index+1:]

print(message)
