words = input().split(' ')
searched_palindrome = input()

palindromes = []
count_palindromes = 0

for i in words:
    if i == i[::-1]:
        palindromes.append(i)
        if i == searched_palindrome:
            count_palindromes += 1


print(palindromes)
print(f"Found palindrome {count_palindromes} times")



# def palindrome(string, palindrome_count):
#     palindromes = []
#     palindrome_count = 0

#     for i in string:
#         if i == i[::-1]:
#             palindromes.append(i)
#             if i == searched_palindrome:
#                 palindrome_count += 1

#     print(palindromes)
#     print(f"Found palindrome {palindrome_count} times")

# words = input().split(' ')
# searched_palindrome = input()

# palindrome(words, searched_palindrome)
