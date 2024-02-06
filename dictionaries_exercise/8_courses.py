def register_name_in_course(courses_info, course_, username):
    if course_ not in courses_info:
        courses_info[course_] = []
    courses_info[course_].append(username)
    return courses_info


def print_result(courses_info):
    for curr_course, data_ in courses_info.items():
        print(f"{curr_course}: {len(courses_info[curr_course])}")
        for curr_name in data_:
            print(f"-- {curr_name}")


def courses_task():
    courses_information = {}
    while True:
        command = input()
        if command == "end":
            break

        data = command.split(" : ")
        course, name = data[0], data[1]
        courses_information = register_name_in_course(courses_information, course, name)

    print_result(courses_information)


courses_task()




# command = input()
# registered_students = {}

# while command != 'end':
#     info = command.split(' : ')
#     course = info[0]
#     name = info[1]

#     if course not in registered_students:
#         registered_students[course] = [name]
#     else:
#         registered_students[course].append(name)

#     command = input()

# for course, names in registered_students.items():
#     print(f"{course}: {len(names)}")
#     for name in names:
#         print(f"-- {name}")


