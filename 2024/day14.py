input = """"""

def parse_robot(input):
    (x, y) = tuple(input.split(' ')[0][2:].split(','))
    (a, b) = tuple(input.split(' ')[1][2:].split(','))
    return (int(x), int(y)), (int(a), int(b))

def wrap(pos):
    (x, y) = pos
    if x < 0:
        x += width
    if x >= width:
        x -= width
    if y < 0:
        y += height
    if y >= height:
        y -= height
    return (x, y)

def move_robots(pos, velocities):
    new_pos = []
    for i in range(len(pos)):
        cur_x, cur_y = pos[i]
        vel_x, vel_y = velocities[i]
        new_pos.append(wrap((cur_x + vel_x, cur_y + vel_y)))
    return new_pos


def aoc_14_1(input):
    pos, vel = [], []
    for robot in input.splitlines():
        (cur_pos, cur_vel) = parse_robot(robot)
        pos.append(cur_pos)
        vel.append(cur_vel)
    for i in range(seconds):
        pos = move_robots(pos, vel)
    quadrants = [0, 0, 0, 0]
    mid_x, mid_y = width // 2, height // 2
    for (x, y) in pos:
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x < mid_x and y > mid_y:
            quadrants[1] += 1
        elif x > mid_x and y < mid_y:
            quadrants[2] += 1
        elif x > mid_x and y > mid_y:
            quadrants[3] += 1
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

width = 101
height = 103
seconds = 100
print(aoc_14_1(input.strip()))