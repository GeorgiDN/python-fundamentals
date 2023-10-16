employees = input().split(' ')
list_employees = [int(i) for i in employees]
happiness_factor = int(input())
improved_happiness = [num * happiness_factor for num in list_employees]

average_happiness = sum(improved_happiness) / len(improved_happiness)
happy_count = sum(h >= average_happiness for h in improved_happiness)
total_count = len(improved_happiness)
message = 'happy' if happy_count >= total_count / 2 else 'not happy'

print(f'Score: {happy_count}/{total_count}. Employees are {message}!')
