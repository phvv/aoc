def valid_elem(cur, rest, after):
    cur = str(cur)
    if not cur in after.keys(): return True
    rule = after[cur]
    for elem in rest:
        if elem in rule:
            return False
    return True

def aoc_5_1(r, o):
    before, after = dict(), dict()
    for rule in r.split('\n'):
        n1, n2 = rule.split('|')[0], rule.split('|')[1]
        if n1 in list(before.keys()):
            before[n1].append(int(n2))
        else:
            before[n1] = [int(n2)]
        if n2 in list(after.keys()):
            after[n2].append(int(n1))
        else:
            after[n2] = [int(n1)]
    valid_orders = []
    for order_s in o.split('\n'):
        order = [int(x) for x in order_s.split(',')]
        valid = True
        for i in range(len(order)):
            cur = order[i]
            rest = order[i + 1:]
            if not valid_elem(cur, rest, after):
                valid = False
                break
        if valid: valid_orders.append(order)
    output = 0
    for order_v in valid_orders:
        output += order_v[len(order_v) // 2]
    return output

def correct_order(o, before, after):
    output = [o[0]]
    for i in range(1, len(o)):
        cur = o[i]
        rule = before[str(cur)]
        inserted = False
        for j in range(len(output)):
            if output[j] in rule:
                output = output[:j] + [cur] + output[j:]
                inserted = True
                break
        if not inserted:
            output += [cur]
    return output

def aoc_5_2(r, o):
    before, after = dict(), dict()
    for rule in r.split('\n'):
        n1, n2 = rule.split('|')[0], rule.split('|')[1]
        if n1 in list(before.keys()):
            before[n1].append(int(n2))
        else:
            before[n1] = [int(n2)]
        if n2 in list(after.keys()):
            after[n2].append(int(n1))
        else:
            after[n2] = [int(n1)]
    valid_orders = []
    for order_s in o.split('\n'):
        order = [int(x) for x in order_s.split(',')]
        valid = True
        for i in range(len(order)):
            cur = order[i]
            rest = order[i + 1:]
            if not valid_elem(cur, rest, after):
                valid = False
                break
        if not valid:
            valid_orders.append(correct_order(order, before, after))
    output = 0
    for order_v in valid_orders:
        output += order_v[len(order_v) // 2]
    return output

input_rules = """"""

input_orders = """"""

print(aoc_5_2(input_rules.strip(), input_orders.strip()))