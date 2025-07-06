goal = "XMAS"

def count_goal(s):
    output = 0
    rev_s = s[::-1]
    for i in range(len(s)):
        if s.startswith(goal, i):
            output += 1
        if rev_s.startswith(goal, i):
            output += 1
    return output

def horiz(s):
    output = 0
    for line in s.split("\n"):
        output += count_goal(line)
    return output

def vert(s):
    output = 0
    line_size = len(s.split("\n")[0])
    for i in range(line_size):
        col = ""
        for line in s.split("\n"):
            col += line[i]
        output += count_goal(col)
    return output

def find_diag(s):
    n_cols = len(s.split("\n")[0])
    n_rows = len(s.split("\n"))
    size = min(n_cols, n_rows)
    output = ""
    for i in range(size):
        output += s.split("\n")[i][i]
    return output

def diag(s):
    output = 0
    line_size = len(s.split("\n")[0])
    # diags across top
    for i in range(line_size):
        new_s = ""
        new_rev_s = ""
        for line in s.split("\n"):
            new_s += line[i:] + "\n"
            new_rev_s += line[::-1][i:] + "\n"
        output += count_goal(find_diag(new_s))
        output += count_goal(find_diag(new_rev_s))
    # diags going down
    for j in range(1, len(s.split("\n"))):
        new_s = ""
        new_rev_s = ""
        for line in s.split("\n")[j:]:
            new_s += line + "\n"
            new_rev_s += line[::-1] + "\n"
        output += count_goal(find_diag(new_s.strip()))
        output += count_goal(find_diag(new_rev_s.strip()))
    return output

def aoc_4_1(s):
    output = 0
    output += horiz(s)
    output += vert(s)
    output += diag(s)
    return output

input = """"""

# print(aoc_4_1(input))

def check_mas(s):
    return s == "MAS" or s[::-1] == "MAS"

def check_xmas(s):
    diag1 = s[0] + s[4] + s[8]
    diag2 = s[2] + s[4] + s[6]
    return check_mas(diag1) and check_mas(diag2)

def aoc_4_2(s):
    output = 0
    lines = s.split("\n")
    for i in range(len(lines) - 2):
        for j in range(len(lines[0]) - 2):
            square = lines[i][j:j+3]
            square += lines[i+1][j:j+3]
            square += lines[i+2][j:j+3]
            output += check_xmas(square)
    return output

print(aoc_4_2(input))