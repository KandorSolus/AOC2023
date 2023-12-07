import collections
f = open("7.txt", "r")
lines = [line.split() for line in f.readlines()]

TYPES = {"HIGHCARD":0, "ONE":1, "TWO":2, "THREE":3, "FULL":4, "FOUR":5, "FIVE":6}

def get_type(hand):
    hand = [*hand]
    counts = collections.Counter(hand)
    js = counts["J"]
    counts.pop('J', None)
    maxCount = None
    if len(counts):
        maxCount = max(counts, key=lambda key: counts[key])
    if maxCount:
        counts[maxCount] += js
    else:
        counts["A"] = 5
        maxCount = "A"
    counts = sorted(counts.values())
    if counts == [5]:
        return (TYPES["FIVE"], maxCount)
    elif counts == [1, 4]:
        return (TYPES["FOUR"], maxCount)
    elif counts == [2, 3]:
        return (TYPES["FULL"], maxCount)
    elif counts == [1, 1, 3]:
        return (TYPES["THREE"], maxCount)
    elif counts == [1, 2, 2]:
        return (TYPES["TWO"], maxCount)
    elif counts == [1, 1, 1, 2]:
        return (TYPES["ONE"], maxCount)
    else:
        return (TYPES["HIGHCARD"], maxCount)

cards = {"T":10, "J":1, "Q":12, "K":13, "A":14}
def compare(first, other):
    first = (first, get_type(first))
    other = (other, get_type(other))
    if first[1][0] == other[1][0]:
        for i in range(5):
            if first[0][i] != other[0][i]:
                val_first = cards[first[0][i]] if not first[0][i].isdigit() else first[0][i]
                val_other = cards[other[0][i]] if not other[0][i].isdigit() else other[0][i]
                return int(val_first) > int(val_other)
        return False
    return first[1] > other[1]

#part1
for i in range(1, len(lines)):
    item = lines[i]
    j = i - 1
    while j >= 0 and compare(lines[j][0], item[0]):
        lines[j + 1] = lines[j]
        j -= 1
    lines[j + 1] = item
print(sum(list(map(lambda x: int(x[1][1]) * (x[0] + 1), enumerate(lines)))))