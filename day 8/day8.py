commands = [line.strip().split() for line in open("input.txt").readlines()]

def parse_commands(command_set):
    accumulator = 0
    command_num = 0
    already_run = set()
    done = False
    while not done:
        if command_num in already_run:
            done = True
            continue
        action, num = command_set[command_num]
        already_run.add(command_num)
        if action == "nop":
            command_num += 1
            continue
        elif action == "acc":
            num = int(num)
            accumulator += num
            command_num += 1
            continue
        elif action == "jmp":
            num = int(num)
            command_num += num
            continue
    return accumulator

test_data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

test_list = [line.strip().split() for line in test_data.split("\n")]

# part 1: answer 1586
results = parse_commands(commands)
print(results)

# part 2: answer 703


class Failure(Exception): pass


def parse_commands2(command_set):
    accumulator = 0
    command_num = 0
    already_run = set()
    done = False
    while not done:
        if command_num in already_run:
            raise Failure()
        if command_num == len(command_set):
            done = True
            continue
        action, num = command_set[command_num]
        already_run.add(command_num)
        if action == "nop":
            command_num += 1
            continue
        elif action == "acc":
            num = int(num)
            accumulator += num
            command_num += 1
            continue
        elif action == "jmp":
            num = int(num)
            command_num += num
            continue

    return accumulator

# par
for counter in range(len(commands)):
    acc = None
    if commands[counter][0] == 'jmp':
        try:
            commands[counter][0] = 'nop'
            acc = parse_commands2(commands)
        except Failure:
            commands[counter][0] = 'jmp'
            continue
        if acc is not None:
            print(acc)
            break
    elif commands[counter][0] == 'nop':
        try:
            commands[counter][0] = 'jmp'
            acc = parse_commands2(commands)
        except Failure:
            commands[counter][0] = 'nop'
            continue
        if acc is not None:
            print(acc)
            break
    else:
        continue

