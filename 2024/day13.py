input = """"""

def parse_button(input):
    # a_x, b_x, p_x
    # a_y, b_y, p_y
    x, y = [], []
    for line in input.splitlines():
        if line[:6] == 'Button':
            x.append(int(line[line.find('+') + 1:line.find(',')]))
            y.append(int(line[line.find('+', line.find('+') + 1) + 1:]))
        else:
            x.append(int(line[line.find('=') + 1:line.find(',')]))
            y.append(int(line[line.find('=', line.find('=') + 1) + 1:]))
    return (tuple(x), tuple(y))

def find_combos(l):
    a, b, p = l
    output = []
    for i in range(min(100, p // a + 1)):
        for j in range(min(100, p // b + 1)):
            cur = a * i + b * j
            if cur == p:
                output += [(i, j)]
            elif cur > p:
                break
    return output

def button_helper(input):
    (x, y) = parse_button(input)
    x_combos = find_combos(x)
    # if x_combos == []: return 0
    y_combos = find_combos(y)
    # if y_combos == []: return 0
    xy_combos = []
    for combo in x_combos:
        if combo in y_combos:
            xy_combos.append(combo)
    output = 0
    for (a, b) in xy_combos:
        coins = 3 * a + b
        if output == 0 or coins < output:
            output = coins
    return output

def aoc_13_1(input):
    output = 0
    for button in input.split('\n\n'):
        output += button_helper(button)
    return output

print(aoc_13_1(input.strip()))