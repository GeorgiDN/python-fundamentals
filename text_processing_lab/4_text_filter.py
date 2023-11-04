ban_list = input().split(', ')
text = input()

for banned_word in ban_list:
    text = text.replace(banned_word, '*' * len(banned_word))

print(text)



# banned_words = input().split(', ')
# text = input()
#
# for word in banned_words:
#     while word in text:
#         text = text.replace(word, '*' * len(word))
#
# print(text)
