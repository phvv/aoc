import re
import string

input = """"""

board = input.strip().splitlines()
n_rows, n_cols = len(board), len(board[0])

def valid_pos(pos):
    row, col = pos
    return row >= 0 and row < n_rows and col >= 0 and col < n_cols

def antinodes(board, c):
    c_pos = []
    for i in range(n_rows):
        for x in re.finditer(c, board[i]):
            c_pos.append((i, x.start()))
    a_pos = []
    for j in range(len(c_pos)):
        j_row, j_col = c_pos[j]
        for k in range(j + 1, len(c_pos)):
            k_row, k_col = c_pos[k]
            delta_row, delta_col = j_row - k_row, j_col - k_col
            new1_row = j_row + delta_row
            new1_col = j_col + delta_col
            new2_row = k_row - delta_row
            new2_col = k_col - delta_col
            if valid_pos((new1_row, new1_col)): a_pos.append((new1_row, new1_col))
            if valid_pos((new2_row, new2_col)): a_pos.append((new2_row, new2_col))
    return a_pos

def aoc_8_1(board):
    valid_pos = set()
    for c in string.ascii_lowercase + string.ascii_uppercase + string.digits:
        for antinode in antinodes(board, c):
            valid_pos.add(antinode)
    return len(valid_pos)

def antinodes2(board, c):
    c_pos = []
    for i in range(n_rows):
        for x in re.finditer(c, board[i]):
            c_pos.append((i, x.start()))
    a_pos = [] + c_pos
    for j in range(len(c_pos)):
        j_row, j_col = c_pos[j]
        for k in range(j + 1, len(c_pos)):
            k_row, k_col = c_pos[k]
            delta_row, delta_col = j_row - k_row, j_col - k_col
            l = 1
            while True:
                new1_row = j_row + (l * delta_row)
                new1_col = j_col + (l * delta_col)
                if not valid_pos((new1_row, new1_col)):
                    break
                a_pos.append((new1_row, new1_col))
                l += 1
            l = 1
            while True:
                new2_row = k_row - (l * delta_row)
                new2_col = k_col - (l * delta_col)
                if not valid_pos((new2_row, new2_col)):
                    break
                a_pos.append((new2_row, new2_col))
                l += 1
            # new1_row = j_row + delta_row
            # new1_col = j_col + delta_col
            # new2_row = k_row - delta_row
            # new2_col = k_col - delta_col
            # if valid_pos((new1_row, new1_col)): a_pos.append((new1_row, new1_col))
            # if valid_pos((new2_row, new2_col)): a_pos.append((new2_row, new2_col))
    return a_pos

def aoc_8_2(board):
    valid_pos = set()
    for c in string.ascii_lowercase + string.ascii_uppercase + string.digits:
        for antinode in antinodes2(board, c):
            valid_pos.add(antinode)
    return len(valid_pos)

print(aoc_8_2(board))