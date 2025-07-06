def pad(b, l):
    return '0' * (l - len(b)) + b

def is_valid_helper(target, rem, ops):
    output = rem[0]
    # if ops == '': return target == output
    # 0 addition, 1 multiplication
    for j in range(len(ops)):
        if ops[j] == '0':
            output += rem[j + 1]
        else:
            output *= rem[j + 1]
    return target == output

def is_valid(target, rem):
    possibilities = 2 ** (len(rem) - 1)
    for i in range(possibilities):
        if is_valid_helper(target, rem, pad(bin(i).replace('0b', ''), len(rem) - 1)):
            return True
    return False

def aoc_7_1(input):
    output = 0
    for line in input.splitlines():
        divide = line.find(':')
        target = int(line[:divide])
        rem = [int(x) for x in line[divide + 2:].split(' ')]
        if is_valid(target, rem):
            output += target
    return output

def base3(n):
    if n == 0: return '0'
    output = ''
    while n > 0:
        output = str(n % 3) + output
        n = n // 3
    return output

input2 = """"""

def is_valid_helper2(target, rem, ops):
    output = rem[0]
    for i in range(len(ops)):
        if ops[i] == '0':
            output += rem[i+1]
        elif ops[i] == '1':
            output *= rem[i+1]
        else:
            output = int(str(output) + str(rem[i + 1]))
        # print(output)
    return output == target
    # agg_rem = []
    # agg_ops = ''
    # for i in range(len(ops)):
    #     if ops[i] != '2':
    #         agg_rem += [rem[0]]
    #         agg_ops += ops[i]
    #         rem = rem[1:]
    #     else:
    #         rem = [int(str(rem[0]) + str(rem[1]))] + rem[2:]
    # agg_rem += [rem[0]]
    # return is_valid_helper(target, agg_rem, agg_ops)
    # print(ops, agg_rem + [rem[0]], agg_ops)

def is_valid2(target, rem):
    possibilities = 3 ** (len(rem) - 1)
    for i in range(possibilities):
        ops = pad(base3(i), len(rem) - 1)
        if is_valid_helper2(target, rem, ops):
            return True
    return False

def aoc_7_2(input):
    output = 0
    for line in input.splitlines():
        divide = line.find(':')
        target = int(line[:divide])
        rem = [int(x) for x in line[divide + 2:].split(' ')]
        if is_valid2(target, rem):
            output += target
    return output



input = """"""



# print(aoc_7_1(input.strip()))
print(aoc_7_2(input.strip()))