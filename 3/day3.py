input = []

with open ('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])


#### Part1 ####
backpacks = []
epic_fails = []
priority  = 0

for line in input:
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    backpacks.append((compartment1, compartment2))

for backpack in backpacks:
    for item in backpack[0]:
        if item in backpack[1]:
            if ord(item) > 96:
                priority += ord(item) - 96
            else:
                priority += ord(item) - 38
            break

print(priority)
