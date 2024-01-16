def take_string_input():
    return input()


def take_int_input():
    return int(input())


def increase_balance(balance_):
    return balance_ + 1


def reduce_balance(balance_):
    return balance_ - 1


def fill_the_list_and_change_balance(bracket, open_br, close_br, balance_):
    if bracket == '(':
        open_br.append(bracket)
        balance_ = increase_balance(balance_)
        return open_br, close_br, balance_

    elif bracket == ')':
        close_br.append(bracket)
        balance_ = reduce_balance(balance_)
        return open_br, close_br, balance_

    return open_br, close_br, balance_


def check_balanced_brackets(lines):
    open_brackets, close_brackets = [], []
    balanced = True
    balance = 0
    for _ in range(lines):
        expression = take_string_input()

        open_brackets, close_brackets, balance = fill_the_list_and_change_balance(
            expression, open_brackets, close_brackets, balance
        )

        if balance > 1 or balance < 0:
            balanced = False
            break

    # Second check
    if balanced:
        if len(open_brackets) != len(close_brackets):
            balanced = False

    if balanced:
        return print('BALANCED')
    else:
        return print('UNBALANCED')


number_of_lines = take_int_input()
check_balanced_brackets(number_of_lines)




##
# lines = int(input())
# open_brackets, close_brackets = [], []
# balanced = True
# balance = 0
#
# for _ in range(lines):
#     expression = input()
#
#     if expression == '(':
#         open_brackets.append(expression)
#         balance += 1
#     elif expression == ')':
#         close_brackets.append(expression)
#         balance -= 1
#
#     if balance > 1 or balance < 0:
#         balanced = False
#         break
#
# # Second check
# if balanced:
#     if len(open_brackets) != len(close_brackets):
#         balanced = False
#
# if balanced:
#     print('BALANCED')
# else:
#     print('UNBALANCED')




##
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
