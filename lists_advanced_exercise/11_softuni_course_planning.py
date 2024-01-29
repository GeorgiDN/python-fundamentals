def add_lesson(lst, lesson):
    if lesson not in lst:
        lst.append(lesson)
    return lst


def insert_lesson_title(lst, lesson, idx):
    if lesson not in lst:
        lst.insert(idx, lesson)
    return lst


def remove(lst, lesson, lesons_with_exr):
    if lesson in lesons_with_exr:
        les_ex_idx = lst.index(lesson) + 1
        lst.pop(les_ex_idx)
        lst.remove(lesson)
        lesons_with_exr.remove(lesson)
    else:
        if lesson in lst:
            lst.remove(lesson)

    return lst, lesons_with_exr


def swap(lst, lesson, lesson2, lesons_with_exr):
    if lesson in lesons_with_exr and lesson2 in lesons_with_exr:
        first_pos = lst.index(lesson)
        sec_pos = lst.index(lesson) + 1
        third_pos = lst.index(lesson2)
        fourth_pos = lst.index(lesson2) + 1
        lst[first_pos] = lesson2
        lst[sec_pos] = f"{lesson2}-Exercise"
        lst[third_pos] = lesson
        lst[fourth_pos] = f"{lesson}-Exercise"

    elif lesson in lesons_with_exr:
        first_pos = lst.index(lesson)
        sec_pos = lst.index(lesson) + 1
        third_pos = lst.index(lesson2)
        lst[first_pos] = lesson2
        lst[sec_pos] = lesson
        lst[third_pos] = f"{lesson2}-Exercise"

    elif lesson2 in lesons_with_exr:
        first_pos = lst.index(lesson)
        sec_pos = lst.index(lesson2)
        third_pos = lst.index(lesson2) + 1
        lst[first_pos] = lesson2
        lst[sec_pos] = f"{lesson2}-Exercise"
        lst[third_pos] = lesson


    else:
        if lesson in lst and lesson2 in lst:
            first_pos = lst.index(lesson)
            sec_pos = lst.index(lesson2)
            lst[first_pos] = lesson2
            lst[sec_pos] = lesson
    return lst


def exercise(lst, lesson, lesons_with_exr):
    for i, curr_lesson in enumerate(lst):
        if lesson == curr_lesson:
            if not lst[i+1] == f"{lesson}-Exercise":
                lst.insert(i+1, f"{lesson}-Exercise")
                lesons_with_exr.append(lesson)
                return lst, lesons_with_exr

    lst.append(lesson)
    lst.append(f"{lesson}-Exercise")
    lesons_with_exr.append(lesson)
    return lst, lesons_with_exr


def course_planning(schedule):
    lessons_with_exercise = []
    while True:
        command = input()
        if command == "course start":
            break

        info = command.split(":")
        action = info[0]

        if action == "Add":
            lesson_title_to_add = info[1]
            schedule = add_lesson(schedule, lesson_title_to_add)

        elif action == "Insert":
            lesson_title_to_insert, index_to_insert = info[1], int(info[2])
            schedule = insert_lesson_title(schedule, lesson_title_to_insert, index_to_insert)

        elif action == "Remove":
            lesson_title_to_remove = info[1]
            schedule, lessons_with_exercise = remove(schedule, lesson_title_to_remove, lessons_with_exercise)

        elif action == "Swap":
            lesson_title1, lesson_title2 = info[1], info[2]
            schedule = swap(schedule, lesson_title1, lesson_title2, lessons_with_exercise)

        elif action == "Exercise":
            lesson_title_exercise = info[1]
            schedule, lessons_with_exercise = exercise(schedule, lesson_title_exercise, lessons_with_exercise)

    return schedule


list_schedule = input().split(", ")
course_planning(list_schedule)
for num, course in enumerate(list_schedule):
    print(f"{num + 1}.{course}")




# schedule = input().split(", ")
# command = input()
# while command != "course start":
#     modification = command.split(":")[0]
#     title = command.split(":")[1]
#     if modification == "Add":
#         if title not in schedule:
#             schedule.append(title)
#     elif modification == "Insert":
#         insert_index = int(command.split(":")[2])
#         if title not in schedule:
#             schedule.insert(insert_index, title)
#     elif modification == "Remove":
#         if title in schedule:
#             remove_index = schedule.index(title)
#             if remove_index + 1 == len(schedule):
#                 schedule.pop()
#             else:
#                 schedule.pop(remove_index)
#                 if schedule[remove_index] == f"{title}-Exercise":
#                     schedule.pop(remove_index)
#     elif modification == "Swap":
#         first_title = title
#         second_title = command.split(":")[2]
#         if first_title in schedule and second_title in schedule:
#             first_title_index = schedule.index(first_title)
#             second_title_index = schedule.index(second_title)
#             schedule[first_title_index], schedule[second_title_index] = \
#                 schedule[second_title_index], schedule[first_title_index]
#     elif modification == "Exercise":
#         if title in schedule:
#             if f"{title}-Exercise" not in schedule:
#                 exercise_index = schedule.index(title) + 1
#                 schedule.insert(exercise_index, f"{title}-Exercise")
#         else:
#             schedule.append(title)
#             schedule.append(f"{title}-Exercise")
#     for lesson in schedule:
#         exercise_letters = len("Exercise")
#         if lesson[-exercise_letters:] == "Exercise":
#             exercise_title = lesson[:-exercise_letters - 1]
#             if schedule.index(exercise_title) + 1 == schedule.index(lesson):
#                 continue
#             else:
#                 current_exercise_index = schedule.index(lesson)
#                 new_exercise_index = schedule.index(exercise_title) + 1
#                 if current_exercise_index > new_exercise_index:
#                     schedule.pop(current_exercise_index)
#                     schedule.insert(new_exercise_index, lesson)
#                 else:
#                     schedule.insert(new_exercise_index, lesson)
#                     schedule.pop(current_exercise_index)
#                 break
#     command = input()
# lesson_counter = 0
# for element in schedule:
#     lesson_counter += 1
#     print(f"{lesson_counter}.{element}")
