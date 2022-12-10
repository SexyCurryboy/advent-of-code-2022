f = open("input.txt", "r")
input = [line.strip() for line in f]
import numpy as np

strenght = 0
cycle = 0
x = 1
def strenght_check(cycle, x):
    global strenght
    if cycle == 20 or (cycle - 20) % 40 == 0:
        strenght += cycle * x
    return(strenght)

image = []
row = 0
def imaging(cycle, x):
    global image
    global row
    if cycle % 40 == 0:
        row += 1
    cycle_image = cycle - (40*row)
    print(cycle_image)
    if cycle_image in [x-1, x, x+1]:
        image.append("#")
    else:
        image.append(".")
    return(image)


def iterate(function, input):
    x = 1
    cycle = 0
    for command in input:
        if command.startswith("noop"):
            cycle += 1
            printer = function(cycle, x)
        elif command.startswith("addx"):
            cycle += 1
            printer = function(cycle, x)
            cycle += 1
            printer = function(cycle, x)
            x += int(command.split()[1])
    return(printer)

print(iterate(strenght_check, input))
screen = ""
for index, pixel in enumerate(iterate(imaging, input)):
    if (index + 1) % 40 == 0:
        screen += pixel + "\n"
    else:
        screen += pixel

print(screen)