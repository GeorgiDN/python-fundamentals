def take_string_input():
    return input()


def take_int_input():
    return int(input())


def increase_balance(bal):
    return bal + 1


def reduce_balance(bal):
    return bal - 1


def check_balanced_brackets(lines):
    balanced = True
    balance = 0
    for _ in range(lines):
        expression = take_string_input()

        if expression == '(':
            balance = increase_balance(balance)
        elif expression == ')':
            balance = reduce_balance(balance)

        if balance > 1 or balance < 0:
            balanced = False
            break

    if balanced:
        return print('BALANCED')
    else:
        return print('UNBALANCED')


number_of_lines = take_int_input()
check_balanced_brackets(number_of_lines)



# lines = int(input())
# balanced = True
# balance = 0

# for _ in range(lines):
#     expression = input()

#     if expression == '(':
#         balance += 1
#     elif expression == ')':
#         balance -= 1

#     if balance > 1 or balance < 0:
#         balanced = False
#         break

# if balanced:
#     print('BALANCED')
# else:
#     print('UNBALANCED')




# number_of_lines = int(input())
# open_bracket = False
# closed_bracket = False
# parentheses_are_balanced = False
# for _ in range(number_of_lines):
#     symbol = input()
#     if symbol == "(":
#         if not open_bracket:
#             open_bracket = True
#         else:
#             parentheses_are_balanced = False
#             break
#     elif symbol == ")":
#         if not open_bracket:
#             parentheses_are_balanced = False
#             break
#         elif not closed_bracket:
#             closed_bracket = True
#             if open_bracket and closed_bracket:
#                 closed_bracket = False
#                 open_bracket = False
#                 parentheses_are_balanced = True
#             else:
#                 parentheses_are_balanced = False
#         else:
#             parentheses_are_balanced = False
#             break
# if parentheses_are_balanced:
#     print("BALANCED")
# else:
#     print("UNBALANCED")
