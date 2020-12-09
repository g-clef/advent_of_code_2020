from itertools import combinations
from collections import deque
inputs = [int(line.strip()) for line in open("input.txt").readlines()]


def find_by_rule(data, preamble_length=25) -> int:
    ring_buffer = deque(maxlen=preamble_length)
    for count in range(len(data)):
        value = data[count]
        if count < preamble_length:
            ring_buffer.append(value)
            continue
        combos = {sum(a) for a in combinations(ring_buffer, 2)}
        if value not in combos:
            return value
        ring_buffer.append(value)


# part 1: answer 27911108
problem_value = find_by_rule(inputs, 25)
print(problem_value)


# part 2:
def find_sums(data, seeked_value):
    for end_counter in range(len(data)):
        end_val = data[end_counter]
        for start_counter in range(end_counter):
            start_val = data[start_counter]

            if start_val > seeked_value or end_val > seeked_value:
                continue
            test = sum(data[start_counter:end_counter])
            if test == seeked_value:
                min_val = min(data[start_counter:end_counter])
                max_val = max(data[start_counter:end_counter])
                return min_val + max_val

print(find_sums(inputs, problem_value))
