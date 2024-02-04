words = input().split(' ')

time_of_occurrences = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in time_of_occurrences:
        time_of_occurrences[word_lower] = 0
    time_of_occurrences[word_lower] += 1

for key, val in time_of_occurrences.items():
    if val % 2 != 0:
        print(key, end=" ")

