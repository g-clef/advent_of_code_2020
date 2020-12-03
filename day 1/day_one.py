from itertools import combinations

inputs = [int(line.strip()) for line in open("input.txt").readlines()]

print([a*b for a, b in combinations(inputs, 2) if a + b == 2020][0])
print([a*b*c for a, b, c in combinations(inputs, 3) if a + b + c == 2020][0])
