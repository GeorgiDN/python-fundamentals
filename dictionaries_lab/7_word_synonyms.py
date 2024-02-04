n = int(input())
synonyms = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
    
    
    
# words_with_synonyms = {}
# rows = int(input())
# 
# for row in range(1, (rows * 2) + 1):
#     if row % 2 != 0:
#         word = input()
#         if word not in words_with_synonyms:
#             words_with_synonyms[word] = []
#     else:
#         synonym = input()
#         words_with_synonyms[word].append(synonym)
# 
# 
# for word_, synonyms in words_with_synonyms.items():
#     print(f"{word_} - {', '.join(synonyms)}")



# n = int(input())
# synonyms = {}
#
# for _ in range(n):
#     word = input()
#     synonym = input()
#
#     if word in synonyms:
#         synonyms[word].append(synonym)
#     else:
#         synonyms[word] = [synonym]
#
# for word, synonym_list in synonyms.items():
#     synonyms_str = ', '.join(synonym_list)
#     print(f'{word} - {synonyms_str}')
