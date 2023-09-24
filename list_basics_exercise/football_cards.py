cards = input()
my_first_list = cards.split()
my_second_list = set(my_first_list)

my_list = list(my_second_list)

count_a = sum(1 for card in my_list if card.startswith('A'))
count_b = sum(1 for card in my_list if card.startswith('B'))

team_a = 11
team_b = 11

team_a_final = team_a - count_a
team_b_final = team_b - count_b

if team_a_final < 7 or team_b_final < 7:
    print(f'Team A - {team_a_final}; Team B - {team_b_final}')
    print('Game was terminated')
else:
    print(f'Team A - {team_a_final}; Team B - {team_b_final}')
