from collections import deque

EMPTY, WALL = ' ', '#'
ROWS = int(input())
matrix = []

for idx in range(ROWS):
    row = list(input())
    matrix.append(row)
    if 'k' in row:
        pl_row, pl_col = idx, row.index('k')

COLS = len(matrix[0])

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def is_valid_index(value, max_value):
    return 0 <= value < max_value


def next_move(pl_row, pl_col, direction):
    d_row, d_col = moves[direction][0], moves[direction][1]
    next_row = (pl_row + d_row) if is_valid_index(pl_row + d_row, ROWS) else None
    next_col = (pl_col + d_col) if is_valid_index(pl_col + d_col, COLS) else None
    return next_row, next_col


max_moves = 0
count_moves = 0
coordinates = deque([(pl_row, pl_col)])
exit_found = False

while coordinates:
    pl_row, pl_col = coordinates.popleft()
    for direction in moves.keys():
        next_row, next_col = next_move(pl_row, pl_col, direction)
        if next_row is None or next_col is None:
            exit_found = True

        if next_row is not None and next_col is not None and matrix[next_row][next_col] == EMPTY:
            coordinates.append((next_row, next_col))
            matrix[next_row][next_col] = 'v'
            count_moves += 1

    if count_moves > max_moves:
        max_moves = count_moves

print(f'Kate got out in {max_moves + 1} moves') if exit_found else print('Kate cannot get out')



#########################################################################################################################
# def correct_lab_bounds(row, col):
#     if row < 0 or col < 0 or row >= len(lab_list) or col >= len(lab_list[0]):
#         return True


# def check_wall(row, col):
#     if lab_list[row][col] in "#v":
#         return True


# def find_exit(row, col):
#     if row == 0 or row == len(lab_list) - 1 or col == 0 or col == len(lab_list[0]):
#         return True


# def find_starting_point():
#     for pos_row, row in enumerate(lab_list):
#         for pos_col, col in enumerate(row):
#             if col == "k":
#                 return pos_row, pos_col


# def find_the_lab_path(row, col, lab):
#     if correct_lab_bounds(row, col) or check_wall(row, col):
#         return

#     steps.append(1)

#     if find_exit(row, col):
#         max_len_path.append(sum(steps))

#     lab[row][col] = "v"
#     find_the_lab_path(row, col + 1, lab)  # check right
#     find_the_lab_path(row, col - 1, lab)  # check left
#     find_the_lab_path(row + 1, col, lab)  # check up
#     find_the_lab_path(row - 1, col, lab)  # check down
#     lab[row][col] = " "

#     steps.pop()


# rows = int(input())
# lab_list = []
# steps = []
# max_len_path = []
# for curr_lab in range(rows):
#     lab_list.append(list(input()))
# cols = len(lab_list[0])
# start_row, start_col = find_starting_point()

# find_the_lab_path(start_row, start_col, lab_list)

# if max_len_path:
#     print(f"Kate got out in {max(max_len_path)} moves")
# else:
#     print("Kate cannot get out")



#############################################################################################################
# def find_position(maze):
#     position = []
#     for row in range(len(maze)):
#         for el in maze[row]:
#             if el == 'k':
#                 position.append(row)
#                 position.append(maze[row].find('k'))
#                 return position
# 
# 
# def next_free_spot(maze):
#     free_spots = []
# 
#     for row in range(len(maze)):
#         for el in range(len(maze[row])):
#             tmp = []
#             if maze[row][el] == ' ':
#                 tmp.append(row)
#                 tmp.append(el)
#                 free_spots.insert(0, tmp)
# 
#     return free_spots
# 
# 
# def find_path(position, next_free, maze):
#     is_blocked = True
#     step = 0
#     moves = 0
# 
#     while step < len(next_free):
#         x1 = next_free[step][0]
#         x2 = next_free[step][1]
#         temp = []
#         temp.append(x1)
#         temp.append(x2)
# # moving left
#         if temp[0] == position[0] and position[1] - temp[1] == 1:
#             position = temp
#             moves += 1
#             next_free.pop(step)
#             step = 0
# # moving right
#         elif temp[0] == position[0] and temp[1] - position[1] == 1:
#             position = temp
#             moves += 1
#             next_free.pop(step)
#             step = 0
# # moving down
#         elif temp[0] - position[0] == 1 and position[1] == temp[1]:
#             position = temp
#             moves += 1
#             next_free.pop(step)
#             step = 0
# # moving up
#         elif position[0] - temp[0] == 1 and position[1] == temp[1]:
#             position = temp
#             moves += 1
#             next_free.pop(step)
#             step = 0
# 
# 
#         else:
# 
#             step += 1
# 
#     if position[0] == 0 or position[0] == (len(maze) -1) or position[1] == 0 or position[1] == len(maze[0]):
#         return f'Kate got out in {moves + 1} moves'
#     return f'Kate cannot get out'
# 
# 
# m_rows = int(input())
# maze = []
# moves = 0
# free_space = True
# for row in range(m_rows):
#     maze.append(input())
# position = find_position(maze)
# next_free = next_free_spot(maze)
# movement = find_path(position, next_free, maze)
# 
# print(movement)
