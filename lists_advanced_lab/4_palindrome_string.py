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

