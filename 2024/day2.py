def is_safe(l):
    prev = int(l[0])
    inc = None
    for level in l[1:]:
        cur = int(level)
        if cur == prev or abs(cur - prev) > 3: return False

        if inc == None:
            inc = cur > prev
        elif inc:
            if cur < prev: return False
        else:
            if cur > prev: return False
        prev = cur
    return True

def aoc_2_1(s):
    output = 0
    for report in s.split("\n"):
        l = report.split(" ")
        for i in range(0, len(l)):
            new_l = l[:i] + l[i+1:]
            if is_safe(new_l):
                output += 1
                break
    return output

input = """"""

print(aoc_2_1(input))