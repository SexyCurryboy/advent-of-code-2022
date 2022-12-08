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

print(forest_helper)

count = 0
for row in forest_helper:
    for tree in row:
        count += int(tree)

print(count)

def check(xb, yb, wald_check):
    global sichtbar
    print("ckeck")
    visible_l = True
    visible_o = True
    visible_r = True
    visible_u = True
    visible = False
    if xb == 0 or xb == lenght - 1:
        visible = True
        return(visible)
    elif yb == 0 or yb == lenght -1:
        visible = True
        return(visible)
    for xk in range(xb):
        print("check 1")
        print("xb=" + str(xb) + ", yb=" + str(yb) + ", xk=" + str(xk) + ", yk=" + str(yb))
        print("baum:" + str(wald_check[xb, yb]) + ", kontrolle:" + str(wald_check[xk, yb]))
        if wald_check[xb, yb] <= wald_check[xk, yb]: #links vom baum
            visible_l = False
    if visible_l:
        visible = True
        return(visible)
    for yk in range(yb):
        print("check 2")
        print("xb=" + str(xb) + ", yb=" + str(yb) + ", xk=" + str(xb) + ", yk=" + str(yk))
        print("baum:" + str(wald_check[xb, yb]) + ", kontrolle:" + str(wald_check[xb, yk]))
        if wald_check[xb, yb] <= wald_check[xb, yk]: #oben vom baum
            visible_o = False
    if visible_o:
        visible = True
        return(visible)
    for xk in range(xb, lenght):
        print("check 3")
        if wald_check[xb, yb] <= wald_check[xk, yb]: #rechts vom baum
            visible_r = False
    if visible_r:
        visible = True
        return(visible)
    for yb in range(yb, lenght):
        print("check 4")
        if wald_check[xb, yb] <= wald_check[xb, yk]: #unten vom baum
            visible_u = False
    if visible_u:
        visible = True
        return(visible)
    if visible:
        sichtbar.append([xb, yb])
    return(visible)            

def is_visible(wald):
    counter = 0
    for yb in range(lenght):
        for xb in range(height):
            if check(xb, yb, wald):
                counter += 1
    return(counter)