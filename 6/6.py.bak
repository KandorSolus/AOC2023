import math

f = open("6.txt", "r")
lines = f.readlines()

def solve(t, d):
    sol = t/2-math.sqrt(t**2/4-d)
    sol = sol + 1 if math.ceil(sol) == sol else math.ceil(sol)
    return (t - 2*sol + 1)

#part1
times = list(map(int, lines[0].split(":")[1].split()))
distances = list(map(int, lines[1].split(":")[1].split()))
sols = 1
for i in range(len(times)):
    t = times[i]
    d = distances[i]
    sols *= solve(t, d)
print(sols)

#part2
t = int("".join(map(str, times)))
d = int("".join(map(str, distances)))
print(solve(t,d))