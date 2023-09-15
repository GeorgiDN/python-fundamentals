
num_of_snowballs = int(input())

highest_snowball_value = 0
highest_snowball_weight = 0
highest_snowball_time = 0
highest_snowball_quality = 0


for num in range(num_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    curr_snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if curr_snowball_value > highest_snowball_value:
        highest_snowball_value = curr_snowball_value
        highest_snowball_weight = snowball_weight
        highest_snowball_time = snowball_time
        highest_snowball_quality = snowball_quality

print(f"{highest_snowball_weight} : {highest_snowball_time} = {int(highest_snowball_value)} ({highest_snowball_quality})")
