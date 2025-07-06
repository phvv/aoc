input = """"""

# pos = (row, col)

board = input.strip().splitlines()
n_rows, n_cols = len(board), len(board[0])

def forward(dir, pos):
    row, col = pos
    if dir == 'up':
        return (dir, (row - 1, col))
    elif dir == 'down':
        return (dir, (row + 1, col))
    elif dir == 'left':
        return (dir, (row, col - 1))
    else: # right
        return (dir, (row, col + 1))

def turn(dir, pos):
    row, col = pos
    if dir == 'up':
        return ('right', (row, col + 1))
    elif dir == 'down':
        return ('left', (row, col - 1))
    elif dir == 'left':
        return ('up', (row - 1, col))
    else: # right
        return ('down', (row + 1, col))

def off_board(pos):
    row, col = pos
    return row < 0 or row >= n_rows or col < 0 or col >= n_cols

def is_blocked(pos):
    row, col = pos
    return board[row][col] == '#'

def aoc_6_1(board):
    for i in range(n_rows):
        if board[i].find("^") != -1:
            pos = (i, board[i].find("^"))
    visited = set()
    dir = 'up'
    while True:
        visited.add((dir, pos))
        (dir1, pos1) = forward(dir, pos)
        (dir2, pos2) = turn(dir, pos)
        if off_board(pos1):
            break
        elif is_blocked(pos1):
            if off_board(pos2):
                break
            else:
                dir, pos = dir2, pos2
        else:
            dir, pos = dir1, pos1
    return visited

def corners_for_up(turns, dir, pos):
    row, col = pos
    # with an up, need a right with row - 1 and col > pos_col; left with col - 1 and row < pos_row
    left = (n_rows, n_cols)
    right = (n_rows, n_cols)
    down = (0, 0)
    for turn in turns:
        turn_dir, (turn_row, turn_col) = turn
        if turn_dir == 'left' and turn_col == col - 1 and turn_row > row:
            left_row, _ = left
            if turn_row < left_row:
                left = (turn_row, turn_col)
        if turn_dir == 'right' and turn_row == row - 1 and turn_col > col:
            _, right_col = right
            if turn_col < right_col:
                right = (turn_row, turn_col)


def aoc_6_2(board):
    route = aoc_6_1(board)
    print(len(route))
    turns = set()
    for step in route:
        dir, pos = step
        if off_board(pos):
            continue
        _, next_pos= forward(dir, pos)
        if is_blocked(next_pos):
            turns.add(step)
    possibilities = set()
    for turn in turns:
        dir, pos = turn

    return turns




print(aoc_6_2(board))


# make visited into a set, every corner thats hit, increment along two lines to see what the next turns are
# check if loop can occur with the next turns found

# maybe hit a corner, find the next along the two lines then do something cool!