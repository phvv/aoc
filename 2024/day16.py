input = """"""

board = input.strip().splitlines()
num_rows, num_cols = len(board), len(board[0])

def move(board, pos, dir, visited, score):
    (x, y) = pos
    if dir == 'u':
        (new_x, new_y) = (x - 1, y)
    elif dir == 'd':
        (new_x, new_y) = (x + 1, y)
    elif dir == 'l':
        (new_x, new_y) = (x, y + 1)
    else:
        (new_x, new_y) = (x, y - 1)
    return (new_x, new_y)

def helper(board, pos, dir, visited, score):
    (x, y) = pos
    if board[x][y] == 'E':
        return score
    (new_x, new_y) = move(board, pos, dir, visited, score)
    helper(board, (new_x, new_y), dir, visited.append((new_x, new_y, dir)), score + 1)



def aoc_16_1(board):
    return helper(board, (num_rows - 2, 1), 'l', [(num_rows - 2, 1, 'l')], 0)

print(aoc_16_1(board))