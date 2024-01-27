def is_palindrome(number):
    return str(number)[::-1] == str(number)


number_list = [x for x in input().split(", ")]
print('\n'.join(str(is_palindrome(num)) for num in number_list))



# def is_palindrome(n):
#     num_str = str(n)
#     reversed_str = num_str[::-1]
#     return num_str == reversed_str


# number_list = list(map(int, input().split(', ')))

# result = '\n'.join(str(is_palindrome(num)) for num in number_list)
# print(result)
