def add_people(people, lst):
    lst[-1] += people
    return lst


def insert_people(idx, people, lst):
    lst[idx] += people
    return lst


def leave_people(idx, people, lst):
    lst[idx] -= people
    return lst


def trains_implement(num_wagons):
    wagons = [0] * num_wagons
    while True:
        command = input()
        if command == "End":
            break

        info = command.split(" ")
        if info[0] == "add":
            people_to_add = int(info[1])
            wagons = add_people(people_to_add, wagons)

        elif info[0] == "insert":
            insert_idx, people_to_insert = int(info[1]), int(info[2])
            wagons = insert_people(insert_idx, people_to_insert, wagons)

        elif info[0] == "leave":
            leave_idx, people_leave = int(info[1]), int(info[2])
            wagons = leave_people(leave_idx, people_leave, wagons)

    return wagons


number_wagons = int(input())
print(trains_implement(number_wagons))



# wagons = [0] * int(input())
#
# while True:
#     command = input().split()
#
#     if command[0] == 'End':
#         print(wagons)
#         break
#
#     elif command[0] == 'add':
#         number_of_people = int(command[1])
#         wagons[-1] += number_of_people
#
#     elif command[0] == 'insert':
#         index = int(command[1])
#         number_of_people = int(command[2])
#         wagons[index] += number_of_people
#
#     elif command[0] == 'leave':
#         index = int(command[1])
#         number_of_people = int(command[2])
#         wagons[index] -= number_of_people



