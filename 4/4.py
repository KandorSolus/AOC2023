f = open("4.txt", "r")

def check_value(lst):
    first = list(filter(len, lst[0]))
    other = list(filter(len, lst[1]))
    score = 0
    for i in range(len(first)):
        if first[i] in other:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score

cards = [line.split(":")[1] for line in f.readlines()]
cards = [card.split("|") for card in cards]
cards = [[val.strip() for val in vals] for vals in cards]
cards = [[val.split(" ") for val in vals] for vals in cards]
cardCounts = [1 for card in cards]
for i, card in enumerate(cards):
    first = list(filter(len, card[0]))
    other = list(filter(len, card[1]))
    wins = 0
    for j in range(len(first)):
        if first[j] in other:
            wins += 1
            if i + wins < len(cards):
                cardCounts[i + wins] += cardCounts[i]
print(sum(cardCounts))