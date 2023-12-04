f = open("3.txt", "r")
lines = f.read().splitlines()
#part1
summ = 0
for y, line in enumerate(lines):
    x = 0
    while x < len(line):
        numlen = 0
        if lines[y][x].isdigit():
            while x < len(line) and lines[y][x].isdigit():
                numlen += 1
                x += 1
            num = int(line[x - numlen : x])
            if any(char not in "0123456789." for i in range(max(0, y - 1), min(len(lines), y + 2)) for char in lines[i][max(0, x - numlen - 1) : min(len(line), x + 1)]):
                summ += num
        else:
            x += 1
print(summ)

#part2
summ = 0
setcount = 0
found = 0
def get_number(line, x, i):
    global found
    global setcount
    setcount += 1
    start = end = x
    while start >= 0 and line[start].isdigit():
        start -= 1
    while end < len(line) and line[end].isdigit():
        end += 1
    found = int(line[start + 1 : end])
    if i >= 60 and i <= 65:
        print("found: ", found, x, i)
    return int(line[start + 1 : end])
count = 0
altsum = 0
altcount = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "*":
            setcount = 0
            lst = list({
                get_number(lines[i], j, i)
                for i in range(max(0, y - 1), min(len(lines) + 1, y + 2))
                for j in range(max(0, x - 1), min(len(line) + 1, x + 2))
                if lines[i][j].isdigit()
            })
            if len(lst) == 2:
                count += 1
                summ += lst[0] * lst[1]
            else:
                altcount += 1
                altsum += lst[0]**2
                print(setcount, lst[0], found, x, y)
print(summ, altsum, count, altcount)

import re

input = open('3.txt', 'r').read()[:-1]

field = {(x, y): c for y, line in enumerate(input.split('\n')) for x, c in enumerate(line)}
part_lines = [(match, y) for y, line in enumerate(input.split('\n')) for match in re.finditer(r'\d+', line)]
part_neighbours = [(int(match.group(0)), [(x, y) for x in range(match.start(0) - 1, match.end(0) + 1) for y in range(i - 1, i + 2)]) for (match, i) in part_lines]

print('part 1:', sum(p for (p, nbs) in part_neighbours if any(field.get(c, '.') not in '0123456789.' for c in nbs)))

gears = [(gear, [part for (part, nbs) in part_neighbours if gear in nbs]) for gear, v in field.items() if v == '*']

print('part 2:', sum(ps[0] * ps[1] for g, ps in gears if len(ps) == 2))
print(len(list(filter(lambda x : len(x[1]) == 1, gears))))