def increase_year(func):
    def wrapper(*args, **kwargs):
        year = args[0] + 1
        while True:
            year_string = str(year)
            if len(set(year_string)) == len(year_string):
                return year
            year += 1
    return wrapper


@increase_year
def find_next_happy_year(curr_year):
    return curr_year


current_year = int(input())
print(find_next_happy_year(current_year))



##########################################################
# def increase_year(year):
#     return year + 1


# def find_next_happy_year(curr_year):
#     while True:
#         curr_year = increase_year(curr_year)
#         year_string = str(curr_year)
#         if len(set(year_string)) == len(year_string):
#             break

#     return curr_year


# current_year = int(input())
# print(find_next_happy_year(current_year))



#################################################################
# year = int(input())

# while True:
#     year += 1
#     year_str = str(year)
#     if len(set(year_str)) == len(year_str):
#         break

# print(year)
