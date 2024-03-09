def my_decorator(original_function):
    def wrapper():
        word = input()

        rev_word = original_function(word)
        print(rev_word)

    return wrapper


@my_decorator
def word_in_reversed(word):
    reversed_word = ''
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]

    return reversed_word


word_in_reversed()



# print(input()[::-1])



# number = int(input())
#
# for i in reversed(str(number)):
#     print(i, end='')



# word = input()
# reversed_word = ''
#
# for i in range(len(word) - 1, -1, -1):
#     reversed_word += word[i]
# print(reversed_word)

