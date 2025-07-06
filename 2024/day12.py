input = """"""

board = input.strip().splitlines()
n_rows, n_cols = len(board), len(board[0])

def letter(pos):
    row, col = pos
    if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
        # invalid pos
        return '.'
    return board[row][col]

def move(dir, pos):
    row, col = pos
    if dir == 'up':     return (row - 1, col)
    elif dir == 'down': return (row + 1, col)
    elif dir == 'left': return (row, col - 1)
    else:               return (row, col + 1)

def analyze(region, pos, known, area, perimeter):
    u_pos = move('up', pos)
    d_pos = move('down', pos)
    l_pos = move('left', pos)
    r_pos = move('right', pos)
    if letter(u_pos) != region:
        perimeter += 1
    elif not u_pos in known:
        (area, perimeter, known) = analyze(region, u_pos, known + [(u_pos)], area + 1, perimeter)
    if letter(d_pos) != region:
        perimeter += 1
    elif not d_pos in known:
        (area, perimeter, known) = analyze(region, d_pos, known + [(d_pos)], area + 1, perimeter)
    if letter(l_pos) != region:
        perimeter += 1
    elif not l_pos in known:
        (area, perimeter, known) = analyze(region, l_pos, known + [(l_pos)], area + 1, perimeter)
    if letter(r_pos) != region:
        perimeter += 1
    elif not r_pos in known:
        (area, perimeter, known) = analyze(region, r_pos, known + [(r_pos)], area + 1, perimeter)
    return (area, perimeter, known)


def aoc_12_1(board):
    output = 0
    analyzed = []
    for i in range(n_rows):
        for j in range(n_cols):
            if not (i, j) in analyzed:
                analyzed.append((i, j))
                area, perimeter, seen = analyze(letter((i, j)), (i, j), [(i, j)], 1, 0)
                analyzed += seen
                output += area * perimeter
    return output

print(aoc_12_1(board))