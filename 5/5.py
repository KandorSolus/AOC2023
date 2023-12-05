import collections

f = open("5.txt", "r")
lines = f.readlines()
seeds = list(map(int, lines[0].split(":")[1].split()))
print(seeds)
ls = -1
lsts = []
for line in lines[1:]:
    if ":" in line:
        ls += 1
        lsts.append([])
    elif len(line.split()) == 3:
        lsts[ls].append(list(map(int, line.split())))
locs = []
printi = 0
for seed in seeds:
    vals = [seed]
    for lst in lsts:
        newVals = []
        for val in vals:
            if printi < 3:
                printi += 1
            newVal = []
            for lis in lst:
                if val >= lis[1] and val <= lis[1]+lis[2]:
                    newVal.append(val - lis[1] + lis[0])
            if len(newVal) == 0:
                newVal = [val]
            newVals.extend(newVal)
        vals = newVals
    locs.append(min(vals))
print(min(locs))