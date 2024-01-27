words = input().split(" ")
palindrome = input()

all_palindromes = [word for word in words if word == word[::-1]]
number_of_searching_palindrome = len([word for word in words if word == palindrome])

print(all_palindromes)
print(f"Found palindrome {number_of_searching_palindrome} times")


# words, palindrome = input().split(" "), input()
# print(f"{[word for word in words if word == word[::-1]]}\n"
#       f"Found palindrome {len([word for word in words if word == palindrome])} times")



# def palindrome(string, palindrome):
#
#     palindromes = [i for i in string if i == i[::-1]]
#     palindrome_count = palindromes.count(palindrome)
#     print(palindromes)
#     print(f"Found palindrome {palindrome_count} times")
#
#
# words = input().split(' ')
# searched_palindrome = input()
#
# palindrome(words, searched_palindrome)



# def palindrome(string, palindrome_count):
#     palindromes = []
#     palindrome_count = 0
#
#     for i in string:
#         if i == i[::-1]:
#             palindromes.append(i)
#             if i == searched_palindrome:
#                 palindrome_count += 1
#
#     print(palindromes)
#     print(f"Found palindrome {palindrome_count} times")
#
#
# words = input().split(' ')
# searched_palindrome = input()
#
# palindrome(words, searched_palindrome)




# words = input().split(' ')
# searched_palindrome = input()
#
# palindromes = []
# count_palindromes = 0
#
# for i in words:
#     if i == i[::-1]:
#         palindromes.append(i)
#         if i == searched_palindrome:
#             count_palindromes += 1
#
#
# print(palindromes)
# print(f"Found palindrome {count_palindromes} times")
