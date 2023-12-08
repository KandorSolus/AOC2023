import collections
f = open("8.txt", "r")
dicts = {}
lines = f.readlines()
algorithm = lines[0].strip()
lines = lines[1:]
#[[dicts[x[0].strip()] = tuple(x[1].strip(" ()").split(", ")) for x in line.split("=")] for line in lines]
for line in lines:
    if "=" in line:
        line = line.split("=")
        dicts[line[0].strip()] = tuple(line[1].strip(" ()\n").split(", "))
keys = list(filter(lambda x: x.endswith("A"), dicts.keys()))
steps = 0
def step(key):
    global steps
    if algorithm[steps % len(algorithm)] == "L":
        key = dicts[key][0]
    else:
        key = dicts[key][1]
    return key

finished = False

while not finished:
    keys = list(map(step, keys))
    steps += 1
    fnished = all(list(map(lambda x: x.endswith("Z"), keys)))

print(steps)