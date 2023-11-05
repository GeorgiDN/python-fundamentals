text = input()
target_char = ":"
emoticons = []

for i in range(len(text) - 1):
    if text[i] == target_char:
        emoticon = text[i:i+2]
        emoticons.append(emoticon)

for emoticon in emoticons:
    print(emoticon)
