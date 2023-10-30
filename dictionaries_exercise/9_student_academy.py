n = int(input())

register_grades = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in register_grades:
        register_grades[name] = [grade]
    else:
        register_grades[name].append(grade)

for name, grades in register_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
