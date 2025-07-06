import re

input = """"""

board = input.strip().splitlines()
n_rows, n_cols = len(board), len(board[0])

def is_valid_pos(pos):
    row, col = pos
    return row >= 0 and row < n_rows and col >= 0 and col < n_cols

def move(dir, pos):
    row, col = pos
    if dir == 'up':     return (row - 1, col)
    elif dir == 'down': return (row + 1, col)
    elif dir == 'left': return (row, col - 1)
    else:               return (row, col + 1)

def valid_move(cur, move, trail):
    cur_row, cur_col = cur
    mv_row, mv_col = move
    if not is_valid_pos(move): return False
    if not int(board[mv_row][mv_col]) - int(board[cur_row][cur_col]) == 1: return False
    if move in trail: return False
    return True

def find_trails(cur_pos, cur_trail, peaks):
    cur_row, cur_col = cur_pos
    if board[cur_row][cur_col] == '9':
        return peaks.append(cur_pos)
    u_row, u_col = move('up', cur_pos)
    d_row, d_col = move('down', cur_pos)
    l_row, l_col = move('left', cur_pos)
    r_row, r_col = move('right', cur_pos)
    if valid_move(cur_pos, (u_row, u_col), cur_trail):
        find_trails((u_row, u_col), cur_trail + [(u_row, u_col)], peaks)
    if valid_move(cur_pos, (d_row, d_col), cur_trail):
        find_trails((d_row, d_col), cur_trail + [(d_row, d_col)], peaks)
    if valid_move(cur_pos, (l_row, l_col), cur_trail):
        find_trails((l_row, l_col), cur_trail + [(l_row, l_col)], peaks)
    if valid_move(cur_pos, (r_row, r_col), cur_trail):
        find_trails((r_row, r_col), cur_trail + [(r_row, r_col)], peaks)
    return peaks

def aoc_10_1(input):
    trailheads = set()
    for x in range(n_rows):
        for y in re.finditer('0', board[x]):
            trailheads.add((x, y.start()))
    trails = dict()
    for trailhead in trailheads:
        trails[trailhead] = list(set(find_trails(trailhead, [trailhead], [])))
    output = 0
    for peaks in trails.values():
        output += len(peaks)
    return output

print(aoc_10_1(board))