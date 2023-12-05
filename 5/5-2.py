import collections
from copy import deepcopy

f = open("5.txt", "r")
lines = f.readlines()
seed_nums = list(map(int, lines[0].split(":")[1].split()))
seeds = []
for i in range(0, len(seed_nums), 2):
    seeds.append([seed_nums[i], seed_nums[i] + seed_nums[i+1] - 1])
ls = -1
lsts = []
for line in lines[1:]:
    if ":" in line:
        ls += 1
        lsts.append([])
    elif len(line.split()) == 3:
        lsts[ls].append(list(map(int, line.split())))


def resolve(seeds, lst):
    i = 0
    while i < len(seeds):
        rng = deepcopy(seeds[i])
        j = 0
        found = False
        while not found and j < len(lst):
            map_values = lst[j]
            map_range = [map_values[1], map_values[1] + map_values[2] - 1]
            #                 rng[0]----rng[1]
            # map_range[0]----------------------map_range[1]
            if rng[0] >= map_range[0] and rng[1] <= map_range[1]:
                seeds[i] = [map_values[0] + (rng[0] - map_values[1]), map_values[0] + (rng[1] - map_values[1])]
                found = True
            #                 rng[0]---------------------------rng[1]
            # map_range[0]----------------------map_range[1]
            elif rng[0] >= map_range[0] and rng[0] <= map_range[1]:
                seeds[i] = [map_values[0] + (rng[0] - map_values[1]), map_values[0] + map_values[2]]
                seeds.append([map_range[1] + 1, rng[1]])
                found = True
            # rng[0]-------------------rng[1]
            #        map_range[0]----------------------map_range[1]
            elif rng[1] >= map_range[0] and rng[1] <= map_range[1]:
                seeds[i] = [map_values[0], map_values[0] + (rng[1] - map_values[1])]
                seeds.append([rng[0], map_range[0] - 1])
                found = True
            # rng[0]-------------------------------rng[1]
            #        map_range[0]-----map_range[1]
            elif rng[0] < map_range[0] and rng[1] > map_range[1]:
                seeds[i] = [map_values[0], map_values[0] + map_values[2]]
                seeds.append([rng[0], map_range[0] - 1])
                seeds.append([map_range[1] + 1, rng[1]])
            j += 1
        i += 1

for lst in lsts:
    resolve(seeds, lst)
print(min(map(lambda x: x[0], seeds)))