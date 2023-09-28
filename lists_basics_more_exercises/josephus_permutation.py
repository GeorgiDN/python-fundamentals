people_in_circle = list(map(int, input().split()))
k = int(input())

output = []
current_index = 0

while people_in_circle:
    index_to_execute = (current_index + k - 1) % len(people_in_circle)
    executed_person = people_in_circle.pop(index_to_execute)
    output.append(str(executed_person))
    current_index = index_to_execute

print("[" + ",".join(output) + "]")
