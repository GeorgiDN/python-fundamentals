my_list = list(map(int, input().split()))

while True:

    text = input()
    if text == 'end':
        break
    else:
     command = text.split()

    if command[0] == 'swap':
        index1 = int(command[1])
        index2 = int(command[2])

        my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

    elif command[0] == 'multiply':
         indx1 = int(command[1])
         indx2 = int(command[2])
         my_list[indx1] *= my_list[indx2]

    elif command[0] == 'decrease':
        for i in range(len(my_list)):
            my_list[i] -= 1

result = ', '.join(map(str, my_list))
print(result)






######################################################################################  CONDITION  ##########################################################################################################################################
# https://judge.softuni.org/Contests/Practice/Index/2474#1
# You are given an array with integers. Write a program to modify the elements after receiving the following commands:
# •	"swap {index1} {index2}" takes two elements and swap their places.
# •	"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index. Save the product at the 1st index.
# •	"decrease" decreases all elements in the array with 1.
# Input
# On the first input line, you will be given the initial array values separated by a single space.
# On the next lines, you will receive commands until you receive the command "end". The commands are as follows: 
# •	"swap {index1} {index2}"
# •	"multiply {index1} {index2}"
# •	"decrease"
# Output
# The output should be printed on the console and consist of elements of the modified array – separated by a comma and a single space ", ".
# Constraints
# •	Elements of the array will be integer numbers in the range [-231...231].
# •	Count of the array elements will be in the range [2...100].
# •	Indexes will be always in the range of the array.




