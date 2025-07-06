def aoc_3_1(s):
    output = 0
    st = "mul("
    enabled = True
    disable = "don't()"
    enable = "do()"
    for i in range(0, len(s)-6):
        if enabled:
            if s[i:i+len(st)] == st:
                end = s[i:].find(')')
                if end <= 11:
                    s1 = s[i+len(st):i+end].split(',', 1)
                    if s1[0].isnumeric() and s1[1].isnumeric():
                        output += int(s1[0]) * int(s1[1])
            elif s[i:i+len(disable)] == disable:
                enabled = False
        else:
            if s[i:i+len(enable)] == enable:
                enabled = True
    return output

input = """"""
print(aoc_3_1(input))