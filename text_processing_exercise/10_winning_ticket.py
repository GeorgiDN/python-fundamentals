import re


def winning_ticket(input_string_):
    formatted_string = re.sub(r'\s+', '', input_string_).replace(',', ' ')
    pattern = re.compile(r'(@{6,10}|\${6,10}|\^{6,10}|\#{6,10})')
    tickets = formatted_string.split(' ')

    for ticket in tickets:
        if len(ticket) != 20:
            print('invalid ticket')
        else:
            left = re.search(pattern, ticket[:len(ticket)//2])
            right = re.search(pattern, ticket[len(ticket)//2:])

            if left is None or right is None:
                print(f'ticket "{ticket}" - no match')
            else:
                left, right = str(left.group()), str(right.group())

                if len(left) == 10 and len(right) == 10:
                    print(f'ticket "{ticket}" - {len(left)}{left[0]} Jackpot!')
                elif left[0] == right[0]:
                    if len(left) < len(right):
                        print(f'ticket "{ticket}" - {len(left)}{left[0]}')
                    elif len(right) < len(left):
                        print(f'ticket "{ticket}" - {len(right)}{right[0]}')
                    elif len(right) == len(left):
                        print(f'ticket "{ticket}" - {len(left)}{left[0]}')
                else:
                    print('invalid ticket')


input_string = input()
winning_ticket(input_string)




##############################################################################################################################
# def check_ticket(ticket):
#     if len(ticket) != 20:
#         return "invalid ticket"
#     special_symbols = ['@', '#', '$', '^']
#     left_part = ticket[:10]
#     right_part = ticket[10:]
#     for match_symbol in special_symbols:
#         for uninterrupted_match_length in range(10, 5, -1):
#             winning_symbols_repetition = match_symbol * uninterrupted_match_length
#             if winning_symbols_repetition in left_part and winning_symbols_repetition in right_part:
#                 if uninterrupted_match_length == 10:
#                     return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
#                 return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
#     return f'ticket "{ticket}" - no match'


# tickets = [x.strip() for x in input().split(", ")]
# for ticket in tickets:
#     print(check_ticket(ticket))




#######################################################################################################################
# def check_ticket_side(ticket_side):
#     uninterrupted_match_length = 0
#     match_symbol = ""
#     for symbol in ticket_side:
#         if symbol != match_symbol:
#             if uninterrupted_match_length >= 6:
#                 break
#             uninterrupted_match_length = 1
#             match_symbol = symbol
#         else:
#             uninterrupted_match_length += 1
#     return uninterrupted_match_length, match_symbol


# tickets = [x.strip() for x in input().split(", ")]
# special_symbols = ['@', '#', '$', '^']
# for ticket in tickets:
#     if len(ticket) != 20:
#         print("invalid ticket")
#     else:
#         if ticket[0] in special_symbols and ticket[0] * 20 == ticket:
#             print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
#         else:
#             first_side = ticket[:10]
#             second_side = ticket[10:]
#             side_one_uninterrupted, side_one_symbol = check_ticket_side(first_side)
#             side_two_uninterrupted, side_two_symbol = check_ticket_side(second_side)
#             winning_length = min(side_one_uninterrupted, side_two_uninterrupted)
#             if side_one_symbol == side_two_symbol and side_two_symbol in special_symbols and winning_length >= 6:
#                 print(f'ticket "{ticket}" - {winning_length}{side_one_symbol}')
#             else:
#                 print(f'ticket "{ticket}" - no match')
