import random
structure = {}
size = 0
dir = ""
path = []
counter = 0

with open("input.txt", "r") as f:
    for line in f:
        if line.startswith("$ cd"):
            dir = line.split()[2]
            if dir == "..":
                structure[path[-1]] += size
                structure[path[-2]] = structure[path[-2]] + structure[path[-1]]
                path.pop()
                size = 0
            else:
                size = 0
                if dir in structure:
                    dir += str(random.randint(1, 999999))
                path.append(dir)
        elif line[0].isdigit(): #loop until doesn't start with digit or dir
            size += int(line.split()[0])
        elif line.startswith("$"): #not listing anymore
            structure[dir] = size

print(structure)


for size in structure.values():
    if size <= 100000:
        counter += size
print(counter)