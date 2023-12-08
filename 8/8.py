import math
f = open("8.txt", "r")
dicts = {}
lines = f.readlines()
algorithm = lines[0].strip()
lines = lines[1:]

for line in lines:
    if "=" in line:
        line = line.split("=")
        dicts[line[0].strip()] = tuple(line[1].strip(" ()\n").split(", "))
keys = list(filter(lambda x: x.endswith("A"), dicts.keys()))
steps = []
def step(key, stept):
    if algorithm[stept % len(algorithm)] == "L":
        key = dicts[key][0]
    else:
        key = dicts[key][1]
    return key

finished = False
lcm = 1
for key in keys:
    stept = 0
    while not key.endswith("Z"):
        key = step(key, stept)
        stept += 1
    steps.append(stept)
print(math.lcm(*steps))