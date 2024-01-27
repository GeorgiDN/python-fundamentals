words = input().split(" ")
print("\n".join([word for word in words if len(word) % 2 == 0]))



# words = input().split(' ')
# words_with_even_length = filter(lambda x: len(x) % 2 == 0, words)
# for word in words_with_even_length:
#     print(word)



# words = input().split(' ')

# for word in words:
#     if len(word) % 2 == 0:
#         print(word)
