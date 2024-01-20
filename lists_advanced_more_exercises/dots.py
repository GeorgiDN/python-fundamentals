from collections import deque


def is_valid(value, max_value):
    return 0 <= value < max_value


def find_dashes(row, col):
    return board[row][col] in "-–"


def already_visited(rol, col):
    return board[rol][col] == "v"


def find_exit(row, col):
    return board[row][col] == "."


def find_the_board_path(row, col, matrix):
    steps = 0
    queue = deque([(row, col)])

    while queue:
        current_row, current_col = queue.popleft()

        if is_valid(current_row, len(matrix)) and is_valid(current_col, len(matrix[0])) \
                and not find_dashes(current_row, current_col) \
                and not already_visited(current_row, current_col):

            steps += 1
            matrix[current_row][current_col] = "v"

            # Add neighboring cells to the queue
            neighbors = [(current_row, current_col + 1),  # right
                         (current_row, current_col - 1),  # left
                         (current_row + 1, current_col),  # up
                         (current_row - 1, current_col)]  # down

            # queue.extend(neighbor for neighbor in neighbors if is_valid(neighbor[0], len(matrix)) and is_valid(neighbor[1], len(matrix[0])))
            for neighbor in neighbors:
                if is_valid(neighbor[0], len(matrix)) and is_valid(neighbor[1], len(matrix[0])):
                    queue.extend([neighbor])

    return steps


rows = int(input())
board = [list(input().split()) for _ in range(rows)]

max_connected_points = max(find_the_board_path(i, j, board) for i in range(rows) for j in range(len(board[i])))
print(max_connected_points)
