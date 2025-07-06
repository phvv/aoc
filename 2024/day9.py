input = """"""

def find_disk(input):
    disk = []
    for i in range(len(input)):
        if i % 2 == 0:
            # file
            file_num = i // 2
            disk += [file_num] * int(input[i])
        else:
            # free
            disk += [-1] * int(input[i])
    return disk

def move_file(cur, disk):
    i = -1
    output = disk
    while True:
        if len(disk) - abs(i) == cur:
            break
        if disk[i] != -1:
            file = disk[i]
            output[cur] = file
            output[i] = -1
            break
        i -= 1
    return output


def arrange(disk):
    for i in range(len(disk)):
        if disk[i] == -1:
            disk = move_file(i, disk)
    return disk

def checksum(disk):
    output = 0
    for i in range(len(disk)):
        if disk[i] != -1:
            output += i * disk[i]
    return output

def aoc_9_1(input):
    disk = find_disk(input)
    arranged_disk = arrange(disk)
    output = checksum(arranged_disk)
    return output

print(aoc_9_1(input.strip()))
