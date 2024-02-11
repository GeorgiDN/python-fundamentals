import math


def bonus_score_system():
    number_of_students = int(input())
    total_number_of_lectures = int(input())
    additional_bonus = int(input())
    bonuses = []
    attendances = []

    for _ in range(number_of_students):
        student_attendances = int(input())
        bonus = student_attendances / total_number_of_lectures * (5 + additional_bonus)
        bonuses.append(bonus)
        attendances.append(student_attendances)

    if bonuses:
        max_bonus = (max(bonuses))
    else:
        max_bonus = 0

    if attendances:
        max_count_of_lectures = (max(attendances))
    else:
        max_count_of_lectures = 0

    print(f"Max Bonus: {math.ceil(max_bonus)}.")
    print(f"The student has attended {max_count_of_lectures} lectures.")


bonus_score_system()
