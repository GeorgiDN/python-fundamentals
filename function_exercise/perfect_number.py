def perfect_number(num):
    divisors = [divisor for divisor in range(1, (num // 2) + 1) if num % divisor == 0]
    if sum(divisors) == num:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))




# def perfect_number(num):
#     divisors = []
#     for divisor in range(1, (num // 2) + 1):
#         if num % divisor == 0:
#             divisors.append(divisor)
# 
#     if sum(divisors) == num:
#         return "We have a perfect number!"
#     return "It's not so perfect."
# 
# 
# number = int(input())
# print(perfect_number(number))




# def perfect_number():
#     sum_of_divisors = 0
#     for i in range(1, number):
#         if number % i == 0:
#             sum_of_divisors += i
#
#     if sum_of_divisors == number:
#         print('We have a perfect number!')
#     else:
#         print("It's not so perfect.")
#
#
# number = int(input())
# perfect_number()
