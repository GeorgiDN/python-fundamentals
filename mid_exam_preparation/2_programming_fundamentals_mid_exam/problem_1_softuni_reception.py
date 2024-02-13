def softuni_reception():
    first_employee_efficiency = int(input())
    second_employee_efficiency = int(input())
    third_employee_efficiency = int(input())
    students_count = int(input())
    hour = 1

    total_hours_employees_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
    while students_count > 0:
        if hour % 4 != 0:
            students_count -= total_hours_employees_efficiency
        hour += 1

    total_hours = hour - 1
    print(f"Time needed: {total_hours}h.")


softuni_reception()


# employ_1 = int(input())
# employ_2 = int(input())
# employ_3 = int(input())

# students = int(input())

# hours = 0

# while True:

#     if students == 0:
#         break
#     if hours > 0:
#         if (hours + 1) % 4 == 0:
#             hours += 1
#             continue

#     for num1 in range(employ_1):
#         if students == 0:
#             break
#         else:
#             students -= 1

#     for num2 in range(employ_2):
#         if students == 0:
#             break
#         else:
#             students -= 1

#     for num3 in range(employ_3):
#         if students == 0:
#             break
#         else:
#             students -= 1

#     hours += 1

# print(f"Time needed: {hours}h.")




######################################################################################  CONDITION  ##########################################################################################################################################
#https://judge.softuni.org/Contests/Practice/Index/2474#0
# Every day, thousands of students pass by the reception at SoftUni with different questions to ask. The employees have to help everyone by providing all the information and answering all of the questions.
# Three employees are working in the reception all day. Each of them can handle a different number of students per hour. Your task is to calculate how much time it will take to answer all the questions of a given number of students.
# First, you will receive 3 lines with integers, representing the number of students that each employee can help per hour. On the following line, you will receive students count as a single integer. 
# Every fourth hour, all employees have a break, so they don't work for an hour. It is the only break for the employees, because they don't need rest, nor have a personal life. Calculate the time needed to answer all the student's questions and print it in the following format: "Time needed: {time}h."
# Input / Constraints
# •	On the first three lines -  each employee efficiency -  integer in the range [1 - 100].
# •	On the fourth line - students count – integer in the range [0 – 10000].
# •	Input will always be valid and in the range specified.
# Output
# •	Print a single line: "Time needed: {time}h."
# •	Allowed working time/memory: 100ms / 16MB.
