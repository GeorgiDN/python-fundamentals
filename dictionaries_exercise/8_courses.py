command = input()
registered_students = {}

while command != 'end':
    info = command.split(' : ')
    course = info[0]
    name = info[1]

    if course not in registered_students:
        registered_students[course] = [name]
    else:
        registered_students[course].append(name)

    command = input()

for course, names in registered_students.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")


