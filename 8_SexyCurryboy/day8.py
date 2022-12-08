import numpy as np
forest = []

with open("input.txt", "r") as f:
    for line in f:
        reihe = []   
        for i in range(len(line)-1):
            reihe.append(int(line[i]))
        forest.append(reihe)

lenght = len(forest[0])
height = len(np.rot90(np.asanyarray(forest), 1))

forest = np.asanyarray(forest)

def check(xi, yi, wald_check):
    for x in range(xi):
        if wald_check[xi, yi] <= wald_check[x, yi]: #wird es mit sich selbst verglichen?
            visible = False
            return(visible)    
    for y in range(yi):
        if wald_check[xi, yi] <= wald_check[xi, y]:
            visible = False
            return(visible)
    for x in range(xi, lenght):
        if wald_check[xi, yi] <= wald_check[x, yi]:
            visible = False
            return(visible)    
    for y in range(yi, lenght):
        if wald_check[xi, yi] <= wald_check[xi, y]:
            visible = False
            return(visible)
    visible = True
            

def is_visible(wald):
    counter = 0
    for xi in range(lenght):
        for yi in range(height):
            if check(xi, yi, wald):
                counter += 1
    return(counter)

print(is_visible(forest))