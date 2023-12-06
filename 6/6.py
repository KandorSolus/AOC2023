import math

f = open("6.txt", "r")
lines = f.readlines()

#part1
times = list(map(int, lines[0].split(":")[1].split()))
distances = list(map(int, lines[1].split(":")[1].split()))
sols = 1
for i in range(len(times)):
    t = times[i]
    d = distances[i]
    sol = t/2-math.sqrt(t**2/4-d)
    sol = sol + 1 if math.ceil(sol) == sol else math.ceil(sol)
    sols *= (t - 2*sol + 1)
print(sols)

#part2
t = int("".join((lines[0].split(":")[1]).split()))
d = int("".join((lines[1].split(":")[1]).split()))
sol = t/2-math.sqrt(t**2/4-d)
sol = sol + 1 if math.ceil(sol) == sol else math.ceil(sol)
sol = (t - 2*sol + 1)
print(sol)