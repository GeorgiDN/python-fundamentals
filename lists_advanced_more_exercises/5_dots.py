from collections import deque

DOT, DASH = '.', '-'
ROWS = int(input())
matrix = [input().split() for _ in range(ROWS)]
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


pl_row, pl_col = 0, 0
max_dots = 0
count_dots = 0
coordinates = deque()

for row in range(ROWS):
    for col in range(COLS):

        coordinates = deque([(row, col)])
        count_dots = 0

        while coordinates:
            pl_row, pl_col = coordinates.popleft()
            for direction in ('up', 'down', 'left', 'right'):
                next_row, next_col = next_move(pl_row, pl_col, direction)
                if next_row is not None and next_col is not None and matrix[next_row][next_col] == DOT:
                    coordinates.append((next_row, next_col))
                    matrix[next_row][next_col] = 'v'
                    count_dots += 1

        if count_dots > max_dots:
            max_dots = count_dots

print(max_dots)


###########################################################################################
# from collections import deque
#
# ROWS = int(input())
# board = [input().split() for _ in range(ROWS)]
# COLS = len(board[0])
# moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#
# def is_valid(row, col):
#     return 0 <= row < ROWS and 0 <= col < COLS
#
#
# def find_max_points(start_row, start_col):
#     queue = deque([(start_row, start_col)])
#     visited.add((start_row, start_col))
#     count = 0
#
#     while queue:
#         row, col = queue.popleft()
#         count += 1
#
#         for dr, dc in moves:
#             next_row, next_col = row + dr, col + dc
#             if is_valid(next_row, next_col) and (next_row, next_col) not in visited and board[next_row][
#                 next_col] == ".":
#                 queue.append((next_row, next_col))
#                 visited.add((next_row, next_col))
#
#     return count
#
#
# visited = set()
# max_connected_dots = 0
#
# for row in range(ROWS):
#     for col in range(COLS):
#         if board[row][col] == "." and (row, col) not in visited:
#             max_connected_dots = max(max_connected_dots, find_max_points(row, col))
#
# print(max_connected_dots)



################################################################################################
# from collections import deque
#
#
# def is_valid(value, max_value):
#     return 0 <= value < max_value
#
#
# def find_dashes(row, col):
#     return board[row][col] in "-"
#
#
# def already_visited(rol, col):
#     return board[rol][col] == "v"
#
#
# def find_exit(row, col):
#     return board[row][col] == "."
#
#
# def find_the_board_path(row, col, matrix):
#     steps = 0
#     queue = deque([(row, col)])
#
#     while queue:
#         current_row, current_col = queue.popleft()
#
#         if is_valid(current_row, len(matrix)) and is_valid(current_col, len(matrix[0])) \
#                 and not find_dashes(current_row, current_col) \
#                 and not already_visited(current_row, current_col):
#
#             steps += 1
#             matrix[current_row][current_col] = "v"
#
#             neighbors = [(current_row, current_col + 1),  # right
#                          (current_row, current_col - 1),  # left
#                          (current_row + 1, current_col),  # up
#                          (current_row - 1, current_col)]  # down
#
#             # queue.extend(neighbor for neighbor in neighbors if is_valid(neighbor[0], len(matrix)) and is_valid(neighbor[1], len(matrix[0])))
#             for neighbor in neighbors:
#                 if is_valid(neighbor[0], len(matrix)) and is_valid(neighbor[1], len(matrix[0])):
#                     queue.extend([neighbor])
#
#     return steps
#
#
# rows = int(input())
# board = [list(input().split()) for _ in range(rows)]
#
# max_connected_points = max(find_the_board_path(i, j, board) for i in range(rows) for j in range(len(board[i])))
# print(max_connected_points)
