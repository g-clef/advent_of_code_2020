import math
field = [line.strip() for line in open("input.txt").readlines()]


def traverse(field, side_step, height_step, pos=0, hit_stuff=""):
    for counter in range(0, len(field), height_step):
        hit_stuff += field[counter][pos]
        pos = (pos + side_step) % len(field[0])
    return hit_stuff.count("#")


print(traverse(field, 3, 1))

steps = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

print(math.prod(traverse(field, right, height) for right, height in steps))
