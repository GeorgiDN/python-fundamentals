students_info = []
searched_course = ""

while True:
    info = input()
    if ":" not in info:
        searched_course = info
        break

    data = info.split(":")
    name, id_, course = data[0], int(data[1]), data[2]
    students_info.append({"name": name, "id": id_, "course": course})

for student in students_info:
    if searched_course.startswith(student["course"][0:2]):
        print(f"{student['name']} - {student['id']}")



# name_with_id = {}
# name_with_course = {}

# searched_course = ""

# while True:
#     info = input()
#     if ":" not in info:
#         searched_course = info
#         break

#     data = info.split(":")
#     name, id_, course = data[0], int(data[1]), data[2]
#     if name not in name_with_id:
#         name_with_id[name] = id_
#     if name not in name_with_course:
#         name_with_course[name] = course

# for name_, course_ in name_with_course.items():
#     if searched_course.startswith(course_[0:3]):
#         print(f"{name_} - {name_with_id[name_]}")



# students = []
# course_to_search = ''

# while True:
#     student_info = input()

#     if ':' not in student_info:
#         course_to_search = student_info
#         break

#     name, ID, course = student_info.split(':')
#     students.append({'name': name, 'ID': ID, 'course': course})

# for student in students:
#     if course_to_search.startswith(student['course'][0:3]):
#         print(f"{student['name']} - {student['ID']}")
      
