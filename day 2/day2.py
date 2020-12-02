import re
inputs = list()

entries = [re.compile(r"(\d+)-(\d+) (\w): (\w+)\n?").match(line).groups() for line in open("input.txt").readlines()]
print(sum(1 for min, max, letter, pw in entries if int(min) <=pw.count(letter) <= int(max)))
print(sum(1 for pos1, pos2, letter, pw in entries if (pw[int(pos1)-1] == letter) ^ (pw[int(pos2)-1] == letter)))
