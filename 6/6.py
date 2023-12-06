import math
import numpy
f = open("6.txt", "r")
lines = f.readlines()

def solve(race):
    sol = race[0]/2-math.sqrt(race[0]**2/4-race[1])
    sol = sol + 1 if math.ceil(sol) == sol else math.ceil(sol)
    return (race[0] - 2*sol + 1)

#part1
times = list(map(int, lines[0].split(":")[1].split()))
distances = list(map(int, lines[1].split(":")[1].split()))
print(numpy.prod(list(map(solve, zip(times, distances)))))

#part2
t = int("".join(map(str, times)))
d = int("".join(map(str, distances)))
print(solve((t, d)))