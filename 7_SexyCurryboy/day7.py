import random
structure = {}
size = 0
dir = ""
path = []
counter = 0

#### Part 1 ####
with open("input.txt", "r") as f:
    for line in f:
        if line.startswith("$ cd"):
            dir = line.split()[2]
            if dir == "..":
                path.pop()
            else:
                if dir in structure:
                    dir += str(random.randint(1, 999999))
                path.append(dir)
        elif line[0].isdigit(): #loop until doesn't start with digit or dir
            for directory in path:
                if directory in structure:
                    structure[directory] += int(line.split()[0])
                else:
                    structure[directory] = int(line.split()[0])

for size in structure.values():
    if size <= 100000:
        counter += size
print(counter)