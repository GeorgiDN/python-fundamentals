def is_valid(lst, idx):
    return 0 <= idx < len(lst)


def add_lesson(list_of_lessons, title):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons


def insert_lesson_title(list_of_lessons, title, idx):
    if is_valid(list_of_lessons, idx):
        if title not in list_of_lessons:
            list_of_lessons.insert(idx, title)
    return list_of_lessons


def remove(list_of_lessons, title, lessons_with_exercise):
    if title in list_of_lessons:
        if title in lessons_with_exercise:
            title_exercice_index = list_of_lessons.index(title) + 1
            list_of_lessons.pop(title_exercice_index)
            list_of_lessons.remove(title)
            lessons_with_exercise.remove(title)
        else:
            list_of_lessons.remove(title)

    return list_of_lessons, lessons_with_exercise


def swap(list_of_lessons, title1, title2, lessons_with_exercise):
    if title1 in lessons_with_exercise and title2 in lessons_with_exercise:
        # first lesson
        first_swap_index = list_of_lessons.index(title1)
        exercise_first_index = list_of_lessons.index(title1) + 1
        # second lesson
        last_swap_index = list_of_lessons.index(title2)
        exercise_last_index = list_of_lessons.index(title2) + 1
        # swap lesson and exercise
        list_of_lessons[first_swap_index] = title2
        list_of_lessons[exercise_first_index] = f"{title2}-Exercise"
        list_of_lessons[last_swap_index] = title1
        list_of_lessons[exercise_last_index] = f"{title1}-Exercise"

    elif title1 in lessons_with_exercise:
        # take the elements
        first_swap_index = list_of_lessons.index(title1)
        index_exercise = list_of_lessons.index(title1) + 1
        last_swap_index = list_of_lessons.index(title2)
        # swap lessons
        list_of_lessons[first_swap_index] = title2
        list_of_lessons[last_swap_index] = title1
        # swap exercise
        curr_exercise = list_of_lessons.pop(index_exercise)
        if list_of_lessons.index(title1) + 1 >= len(list_of_lessons):
            list_of_lessons.append(curr_exercise)
        else:
            list_of_lessons.insert(list_of_lessons.index(title1) + 1, curr_exercise)

    elif title2 in lessons_with_exercise:
        first_swap_index = list_of_lessons.index(title1)
        last_swap_index = list_of_lessons.index(title2)
        index_exercise = list_of_lessons.index(title2) + 1
        # swap lessons
        list_of_lessons[first_swap_index] = title2
        list_of_lessons[last_swap_index] = title1
        # swap exercise
        curr_exercise = list_of_lessons.pop(index_exercise)
        if list_of_lessons.index(title2) + 1 >= len(list_of_lessons):
            list_of_lessons.append(curr_exercise)
        else:
            list_of_lessons.insert(list_of_lessons.index(title2) + 1, curr_exercise)

    else:
        if title1 in list_of_lessons and title2 in list_of_lessons:
            first_swap_index = list_of_lessons.index(title1)
            last_swap_index = list_of_lessons.index(title2)
            list_of_lessons[first_swap_index] = title2
            list_of_lessons[last_swap_index] = title1
    return list_of_lessons


def exercise(list_of_lessons, title, lessons_with_exercise):
    if title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(f"{title}-Exercise")
        lessons_with_exercise.append(title)
        return list_of_lessons, lessons_with_exercise

    else:
        if title not in lessons_with_exercise:
            if list_of_lessons.index(title) + 1 < len(list_of_lessons):
                list_of_lessons.insert(list_of_lessons.index(title) + 1, f"{title}-Exercise")
            else:
                list_of_lessons.append(f"{title}-Exercise")
                lessons_with_exercise.append(title)

    return list_of_lessons, lessons_with_exercise


def course_planning(schedule):
    lesson_titles_with_exercises = []
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
            schedule, lesson_titles_with_exercises = remove(schedule, lesson_title_to_remove, lesson_titles_with_exercises)

        elif action == "Swap":
            lesson_title1, lesson_title2 = info[1], info[2]
            schedule = swap(schedule, lesson_title1, lesson_title2, lesson_titles_with_exercises)

        elif action == "Exercise":
            lesson_title_exercise = info[1]
            schedule, lesson_titles_with_exercises = exercise(schedule, lesson_title_exercise, lesson_titles_with_exercises)

    return schedule


list_schedule = input().split(", ")
course_planning(list_schedule)
for index_, course in enumerate(list_schedule):
    print(f"{index_ + 1}.{course}")





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
