import numpy as np
forest = []
sichtbar = []
with open("input.txt", "r") as f:
    for line in f:
        reihe = []   
        for i in range(len(line)-1):
            reihe.append(int(line[i]))
        forest.append(reihe)

lenght = len(forest[0])
height = len(forest)
forest = np.asanyarray(forest)
forest_helper = np.full((height, lenght), 0)

for ver in range(1, height - 1): #oberste & unterste Reihe eh True
    #links nach rechts
    highest = 0
    for hor in range(lenght - 1): #links & rechts eh True, aber Wert links relevant
        if highest < forest[ver][hor]:
            forest_helper[ver][hor] = 1
            highest = forest[ver][hor]
    #rechts nach links
    highest = 0
    for hor in range(lenght - 1, -1, -1): #links & rechts eh True, aber Wert rechts relevant
        if highest < forest[ver][hor]:
            forest_helper[ver][hor] = 1
            highest = forest[ver][hor]

for hor in range(1, lenght - 1): #oberste & unterste Reihe eh True
    #oben nach unten
    highest = 0
    for ver in range(height - 1): #oben & unten eh True, aber Wert oben relevant
        if highest < forest[ver][hor]:
            forest_helper[ver][hor] = 1
            highest = forest[ver][hor]
    #unten nach oben
    highest = 0
    for ver in range(height - 1, -1, -1): #oben & unten eh True, aber Wert unten relevant
        if highest < forest[ver][hor]:
            forest_helper[ver][hor] = 1
            highest = forest[ver][hor]
            
for ver in range(lenght):
    forest_helper[ver][0] = 1
    forest_helper[ver][height - 1] = 1

for hor in range(height):
    forest_helper[0][hor] = 1
    forest_helper[lenght - 1][hor] = 1

count = 0
for row in forest_helper:
    for tree in row:
        count += int(tree)
print(count)

forest_helper_scenic = np.full((height, lenght), 1)

for ver in range(height - 1):
    #links nach rechts
    tree_height = 0
    sight = 0
    for hor in range(lenght - 1):
        if tree_height >= forest[ver][hor]:
            forest_helper_scenic[ver][hor] = sight
            sight += 1
        if tree_height < forest[ver][hor]:
            tree_height = forest[ver][hor]
            sight += 1

    #rechts nach links
    tree_height = 0
    sight = 0
    for hor in range(lenght - 1, -1, -1):
        if tree_height >= forest[ver][hor]:
            forest_helper_scenic[ver][hor] = forest_helper_scenic[ver][hor] * sight
            sight += 1
        if tree_height < forest[ver][hor]:
            tree_height = forest[ver][hor]
            sight += 1

for hor in range(lenght - 1):
    #oben nach unten
    tree_height = 0
    sight = 0
    for ver in range(height - 1):
        if tree_height >= forest[ver][hor]:
            forest_helper_scenic[ver][hor] = forest_helper_scenic[ver][hor] * sight
            sight += 1
        if tree_height < forest[ver][hor]:
            tree_height = forest[ver][hor]
            sight += 1
    #unten nach oben
    tree_height = 0
    for ver in range(height - 1, -1, -1):
        if tree_height >= forest[ver][hor]:
            forest_helper_scenic[ver][hor] = forest_helper_scenic[ver][hor] * sight
            sight += 1
        if tree_height < forest[ver][hor]:
            tree_height = forest[ver][hor]
            sight += 1

print(forest_helper_scenic)