number_list = list(map(int, input().split()))

average_number = sum(number_list) / len(number_list)
numbers_greater_than_average = []

number_list = sorted(number_list, reverse=True)

count_five_numbers = 5
for num in number_list:
    if count_five_numbers == 0:
        break
    elif num > average_number:
        numbers_greater_than_average.append(num)
        count_five_numbers -= 1

if numbers_greater_than_average:
    result = ' '.join(map(str, numbers_greater_than_average))
    print(result)
else:
    print('No')





######################################################################################  CONDITION  ##########################################################################################################################################
#https://judge.softuni.org/Contests/Practice/Index/2474#2
# Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value in the sequence, sorted in descending order.
# Input
# •	Read from the console a single line holding space-separated integers.
# Output
# •	Print the above-described numbers on a single line, space-separated. 
# •	If less than 5 numbers hold the property mentioned above, print less than 5 numbers. 
# •	Print "No" if no numbers hold the above property.
