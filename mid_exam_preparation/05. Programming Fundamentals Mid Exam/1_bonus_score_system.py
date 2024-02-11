import math


class BonusScoreSystem:

    def __init__(self, number_of_students, total_number_of_lectures, additional_bonus):
        self.number_of_students = number_of_students
        self.total_number_of_lectures = total_number_of_lectures
        self.additional_bonus = additional_bonus
        self.bonuses = []
        self.attendances = []

    def bonus_score_system_task_implementation(self):
        for _ in range(self.number_of_students):
            student_attendances = int(input())
            bonus = student_attendances / self.total_number_of_lectures * (5 + self.additional_bonus)
            self.bonuses.append(bonus)
            self.attendances.append(student_attendances)

        if self.bonuses:
            max_bonus = (max(self.bonuses))
        else:
            max_bonus = 0

        if self.attendances:
            max_count_of_lectures = (max(self.attendances))
        else:
            max_count_of_lectures = 0

        print(f"Max Bonus: {math.ceil(max_bonus)}.")
        print(f"The student has attended {max_count_of_lectures} lectures.")


students = int(input())
number_of_lectures = int(input())
bonus_additional = int(input())
bonus_score_system = BonusScoreSystem(students, number_of_lectures, bonus_additional)
bonus_score_system.bonus_score_system_task_implementation()



# import math


# def bonus_score_system():
#     number_of_students = int(input())
#     total_number_of_lectures = int(input())
#     additional_bonus = int(input())
#     bonuses = []
#     attendances = []

#     for _ in range(number_of_students):
#         student_attendances = int(input())
#         bonus = student_attendances / total_number_of_lectures * (5 + additional_bonus)
#         bonuses.append(bonus)
#         attendances.append(student_attendances)

#     if bonuses:
#         max_bonus = (max(bonuses))
#     else:
#         max_bonus = 0

#     if attendances:
#         max_count_of_lectures = (max(attendances))
#     else:
#         max_count_of_lectures = 0

#     print(f"Max Bonus: {math.ceil(max_bonus)}.")
#     print(f"The student has attended {max_count_of_lectures} lectures.")


# bonus_score_system()
