def aoc_1_1(s):
    l1, l2 = [], []
    for line in s.split("\n"):
        n = line.split("   ")
        l1.append(int(n[0]))
        l2.append(int(n[-1]))
    l1.sort()
    l2.sort()
    output = 0
    for i in range(0, len(l1)):
        output += abs(l1[i] - l2[i])
    return output

def aoc_1_2(s):
    l1, l2 = [], []
    for line in s.split("\n"):
        n = line.split("   ")
        l1.append(int(n[0]))
        l2.append(int(n[-1]))
    instances = dict()
    for elem in l2:
        instances[elem] = instances.get(elem, 0) + 1
    output = 0
    for elem in l1:
        output += instances.get(elem, 0) * elem
    return output

input = """"""

print(aoc_1_2(input))