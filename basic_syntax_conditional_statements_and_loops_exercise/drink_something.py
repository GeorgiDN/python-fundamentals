def get_drink(age):
    age_ranges = {
        (0, 14): 'drink toddy',
        (15, 18): 'drink coke',
        (19, 21): 'drink beer',
        (22, float('inf')): 'drink whisky'
    }

    for age_range, drink in age_ranges.items():
        if age_range[0] <= age <= age_range[1]:
            return drink


current_age = int(input())
result = get_drink(current_age)
print(result)





###
# ages = {"drink toddy": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
#         "drink coke": [15, 16, 17, 18],
#         "drink beer": [19, 20, 21]
#         }

# age = int(input())
# if age in ages["drink toddy"]:
#     print("drink toddy")
# elif age in ages["drink coke"]:
#     print("drink coke")
# elif age in ages["drink beer"]:
#     print("drink beer")
# else:
#     print('drink whisky')



###
# age = int(input())

# if age <= 14:
#     print('drink toddy')
# elif 14 < age <= 18:
#     print('drink coke')
# elif 18 < age <= 21:
#     print('drink beer')
# elif age > 21:
#     print('drink whisky')
