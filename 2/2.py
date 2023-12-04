f = open("2.txt", "r")
MAX_BLUE = 14
MAX_GREEN = 13
MAX_RED = 12
def check_possible(game):
    for sub in game[1]:
        for value in sub:
            value = value.strip()
            value = value.split(" ")
            if (value[1] == "blue" and int(value[0]) > MAX_BLUE 
            or value[1] == "green" and int(value[0]) > MAX_GREEN
            or value[1] == "red" and int(value[0]) > MAX_RED):
                return False
    return True
def check_minimum(game):
    blue = 0
    green = 0
    red = 0
    for sub in game[1]:
        for value in sub:
            value = value.strip()
            value = value.split(" ")
            if value[1] == "blue" and int(value[0]) > blue:
                blue = int(value[0])
            if value[1] == "green" and int(value[0]) > green:
                green = int(value[0])
            if value[1] == "red" and int(value[0]) > red:
                red = int(value[0])
    return blue * green * red
            
games = [line.split(":") for line in f.readlines()]
print("games")
print(games)
sub_sets = [[game[0], game[1].split(";")] for game in games]
print("sub_sets")
print(sub_sets)
values = [[sub[0], [subsub.split(",") for subsub in sub[1]]] for sub in sub_sets]
print("values")
print(values[0])
#values = list(filter(check_possible, values))
sum_of_powers = sum(map(check_minimum, values))
print("result")
print(sum_of_powers)
#game_nums = [int(game[0].split(" ")[1]) for game in values]
#print(sum(game_nums))