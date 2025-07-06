input = """"""

def parse_input(input):
    moves = input.split('\n\n')[1].replace('\n', '')
    rows = input.split('\n\n')[0].splitlines()
    board = []
    for row in rows:
        board.append([])
        for c in row:
            board[-1].append(c)
    return (board, moves)

def move_pos(board, dir, pos):
    (x, y) = pos
    if dir == '^':
        (new_x, new_y) = (x - 1, y)
    elif dir == 'v':
        (new_x, new_y) = (x + 1, y)
    elif dir == '>':
        (new_x, new_y) = (x, y + 1)
    else:
        (new_x, new_y) = (x, y - 1)
    return ((new_x, new_y), board[new_x][new_y])

def find_path(board, dir, pos):
    path, coordinates = [], []
    num_rows, num_cols = len(board), len(board[0])
    # print(num_rows, num_cols)
    cur_pos = pos
    # print("finding path...")
    while True:
        ((next_x, next_y), next_path) = move_pos(board, dir, cur_pos)
        # print(((next_x, next_y), next_path))
        path.append(next_path)
        coordinates.append((next_x, next_y))
        cur_pos = (next_x, next_y)
        # if next_x <= 0 or next_x >= (num_rows - 1) or next_y <= 0 or next_y >= (num_cols - 1):
        if next_path == '#':
            break
        if next_path == '.':
            break
    return path, coordinates

def insert_path(board, path, coordinates):
    for i in range(len(path)):
        (x, y) = coordinates[i]
        board[x][y] = path[i]
    return board

def move(board, dir, pos):
    (x, y) = pos
    ((dir_x, dir_y), dir_space) = move_pos(board, dir, pos)
    if dir_space == '#':
        return (board, pos)
    elif dir_space == '.':
        board[dir_x][dir_y] = '@'
        board[x][y] = '.'
        return (board, (dir_x, dir_y))
    else:
        # move those boxes!
        path, coordinates = find_path(board, dir, pos)
        if not '.' in path:
            return (board, pos)
        new_path = path[::-1]
        board = insert_path(board, new_path, coordinates)
        board[dir_x][dir_y] = '@'
        board[x][y] = '.'
        return (board, (dir_x, dir_y))


def helper(board, moves, pos):
    for dir in moves:
        board, pos = move(board, dir, pos)
    return board

def aoc_15_1(input):
    board, moves = parse_input(input)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '@':
                pos = (i, j)
    board = helper(board, moves, pos)
    output = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                output += i * 100 + j
    return output

print(aoc_15_1(input.strip()))