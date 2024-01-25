def grades(curr_grade):
    if 2.00 <= curr_grade <= 2.99:
        return "Fail"
    elif 3.00 <= curr_grade <= 3.49:
        return "Poor"
    elif 3.50 <= curr_grade <= 4.49:
        return "Good"
    elif 4.50 <= curr_grade <= 5.49:
        return "Very Good"
    elif 5.50 <= curr_grade <= 6.00:
        return "Excellent"


grade = float(input())
print(grades(grade))




# def grades(curr_grade):
#     return next((grade_name for grade_range, grade_name in [
#         ((2.00, 2.99), "Fail"),
#         ((3.00, 3.49), "Poor"),
#         ((3.50, 4.49), "Good"),
#         ((4.50, 5.49), "Very Good"),
#         ((5.50, 6.00), "Excellent"),
#     ] if grade_range[0] <= curr_grade <= grade_range[1]), None)
#
#
# grade = float(input())
# print(grades(grade))




# grade = float(input())
# print(next((grade_name for grade_range, grade_name in [
#         ((2.00, 2.99), "Fail"),
#         ((3.00, 3.49), "Poor"),
#         ((3.50, 4.49), "Good"),
#         ((4.50, 5.49), "Very Good"),
#         ((5.50, 6.00), "Excellent"),
#     ] if grade_range[0] <= grade <= grade_range[1]), None))



# grade_data = float(input())
#
#
# def solve(grade):
#     if 2.00 <= grade <= 2.99:
#         return 'Fail'
#     elif 3.00 <= grade <= 3.49:
#         return 'Poor'
#     elif 3.50 <= grade <= 4.49:
#         return 'Good'
#     elif 4.50 <= grade <= 5.49:
#         return 'Very Good'
#     elif 5.50 <= grade <= 6.0:
#         return 'Excellent'
#
# print(solve(grade_data))
