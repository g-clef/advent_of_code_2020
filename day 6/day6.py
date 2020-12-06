# part 1 answer 6161
def read_input():
    results = list()
    accumulator = set()
    for line in open("input.txt").readlines():
        line = line.strip()
        if not line:
            results.append(accumulator)
            accumulator = set()
        line = list(line)
        accumulator.update(set(line))
    if accumulator:
        results.append(accumulator)
    return results


data = read_input()
print(sum([len(entry) for entry in data]))


# part 2: answer 2971
def read_input2():
    results = list()
    accumulator = None
    for line in open("input.txt").readlines():
        line = line.strip()
        if not line:
            results.append(accumulator)
            accumulator = None
            continue
        line = list(line)
        if accumulator is None:
            accumulator = set(line)
        else:
            accumulator.intersection_update(set(line))

    if accumulator:
        results.append(accumulator)
    return results


data2 = read_input2()
print(sum([len(entry) for entry in data2]))