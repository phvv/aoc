input = ""

def is_even(n):
    return n % 2 == 0

def num_digits(n):
    return len(str(n))

def split_stone(n):
    mid = num_digits(n) // 2
    l = int(str(n)[:mid])
    r = int(str(n)[mid:])
    return [l, r]

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif is_even(num_digits(stone)):
            new_stones += split_stone(stone)
        else:
            new_stones.append(stone * 2024)
    return new_stones

def aoc_11_1(input, num_blinks):
    stones = [int(x) for x in input.split(' ')]
    for i in range(num_blinks):
        stones = blink(stones)
    return len(stones)

print(aoc_11_1(input, 25))
